import urllib.request

"""
Luke 11: Sledestans
https://julekalender.knowit.no/doors/ck4006l3gefub0109eto9igva
"""

input_file = (
    urllib.request
    .urlopen("https://julekalender.knowit.no/resources/2019-luke11/terreng.txt")
    )

landing_strip = [c for c in input_file.read().decode()]
vel = 10703437
terrain = {
    'G' : -27,
    'I' : 12,
    'A' : -59,
    'S' : -212,
    'F1' : -70,
    'F2' : 35
}

distance = 0

ice_index = mountain_index = 1
for km in landing_strip:
    if vel <= 0:
        print(distance)
        break

    if km != 'I':
        ice_index = 1

    if km == 'F':
        if mountain_index == 1:
            km = 'F1'
            mountain_index = 2
        else:
            km = 'F2'
            mountain_index = 1

    vel += (terrain[km]*ice_index)
    distance += 1

    if km == 'I':
        ice_index += 1
