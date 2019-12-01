import numpy as np
import urllib.request

"""
Luke 1: Drageproblemer
https://julekalender.knowit.no/doors/ck3ln1prramud0109sqetdk7g
"""

input_file = (
    urllib.request
    .urlopen("https://knowit-julekalender.s3.eu-central-1.amazonaws.com/sau.txt")
    )
tribute = np.loadtxt(input_file , delimiter=", ")

dragon_size = 50
dragon_sanity = INITIAL_SANITY = 5
left_over = days_of_survival = 0

for day in tribute:
    #num of sheep available
    tribute_of_the_day = day + left_over

    left_over = 0

    if dragon_size <= tribute_of_the_day:
        dragon_sanity = INITIAL_SANITY
        left_over = tribute_of_the_day - dragon_size
        dragon_size += 1
    else:
        dragon_sanity -= 1
        if dragon_sanity <= 0:
            break
        dragon_size -= 1
        left_over = 0

    days_of_survival += 1

print(days_of_survival)
