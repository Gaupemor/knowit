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
INITIAL_SANITY = dragon_sanity = 5
days_of_survival = tribute_left_over = 0

for intitial_tribute in tribute:
    daily_tribute = intitial_tribute + tribute_left_over

    if dragon_size <= daily_tribute:
        dragon_sanity = INITIAL_SANITY
        tribute_left_over = daily_tribute - dragon_size
        dragon_size += 1
    else:
        dragon_sanity -= 1
        if dragon_sanity <= 0:
            break
        dragon_size -= 1
        tribute_left_over = 0

    days_of_survival += 1

print(days_of_survival)
