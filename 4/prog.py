import pandas as pd
import numpy as np

"""
Luke 4: Piratsneglen Sneglulf og skattekartet hans
https://julekalender.knowit.no/doors/ck3q4m03ubk5y0109bquxtumd
"""

data = pd.read_csv("https://knowit-julekalender.s3.eu-central-1.amazonaws.com/2019-luke4/coords.csv")

# create data frame of coordinates in csv file
coor = pd.DataFrame(data).dropna().values
map = np.zeros((1000, 1000))

time_spent = 0
current_pos = np.array([0, 0])

# starts at (0, 0)
for x, y in coor:
    distance_x = x - current_pos[0]
    distance_y = y - current_pos[1]

    def go_east():
        current_pos[1] += 1
    def go_west():
        current_pos[1] -= 1
    def go_north():
        current_pos[0] -= 1
    def go_south():
        current_pos[0] += 1
    def calc_time():
        map[current_pos[0], current_pos[1]] += 1
        return int(map[current_pos[0], current_pos[1]])


    # 1st horizontal - x
    go_direction = (go_south if distance_x > 0 else go_north)

    for x_step in range(abs(distance_x)):
        go_direction()
        time_spent += calc_time()

    # 2nd horizontal - y
    go_direction = (go_east if distance_y > 0 else go_west)

    for y_step in range(abs(distance_y)):
        go_direction()
        time_spent += calc_time()

print(time_spent)
