import numpy as np
import urllib.request
import sys
sys.setrecursionlimit(3000)

"""
Luke 2: Syndefloden
https://julekalender.knowit.no/doors/ck3n9yxzraz7h0109wu72kzoo
"""

input_file = (
    urllib.request
    .urlretrieve("https://knowit-julekalender.s3.eu-central-1.amazonaws.com/2019-luke2/world.txt")
    )

# open entire file initially

world = np.array([list(w) for w in [w.replace('\n', '')
    for w in np.array(open('world.txt', 'r').readlines())]])
#print(world)
unique, counts = np.unique(world, return_counts=True)
print(dict(zip(unique, counts)))

water = 0

def flood_fill(r, c):
    if world[r][c] != ' ':
        return
    else:
        world[r][c] = '.'
        if r != 0:
            flood_fill(r-1, c)
        if c != 0:
            flood_fill(r, c-1)
        if r < world.shape[0] - 1:
            flood_fill(r+1, c)
        if c < world.shape[0]:
            flood_fill(r, c+1)

flood_fill(0, 0)
flood_fill(0, 2999)
#print(world)



for row in range(world.shape[0]):
    start = False
    first_set = -1
    for col in range(world.shape[1]):
        if world[row][col] == '#' and not start:
            start = True
        if start and world[row][col] == '.' and first_set == -1:
            first_set = col
        elif world[row][col] == '#' and first_set != -1:
            end = col
            world[row][first_set] = '~'
            first_set += 1
            while first_set != end:
                world[row][first_set] = '~'
                first_set += 1
            first_set = -1
            start = False

for row in range(world.shape[0]):
    for col in range(world.shape[1]):
        if world[row][col] == '.':
            world[row][col] = ' '

unique, counts = np.unique(world, return_counts=True)
print(dict(zip(unique, counts)))
