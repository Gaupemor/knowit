import numpy as np
import urllib.request
import sys

"""
Luke 8: Lotto-Lotte feirer jul i Vegas
https://julekalender.knowit.no/doors/ck3vz7az2czyv0109y0s5nbud
"""

sys.setrecursionlimit(3000)

# 10 hjul, 4 operasjoner
original_wheels = np.empty((10, 4), dtype=object)

with (
    urllib.request
    .urlopen("https://knowit-julekalender.s3.eu-central-1.amazonaws.com/2019-luke8/wheels.txt")
    ) as f:

    for i in range(0, original_wheels.shape[0]):
        operations = np.array((f.readline().decode('utf-8')).split(': ')[1].strip('\n').split(', '))
        original_wheels[i] = operations

gevinst = 0

def play(wheel_states, winnings):
    index = int(str(winnings)[len(str(winnings)) - 1])
    o = wheel_states[index][0]
    if o == 'STOPP':
        return winnings
    elif 'PLUSS' in o:
        if 'TILPAR' in o:
            w_str = str(abs(winnings))
            w_str = ''.join([x if int(x) % 2 != 0 else str((int(x) + 1) % 10) for x in w_str])
            w = int(w_str)
            if winnings < 0:
                w = -w
            winnings = w
        else:
            winnings += int(o.split('PLUSS')[1])
    elif 'MINUS' in o:
        winnings -= int(o.split('MINUS')[1])
    elif 'TREKK' in o:
        w_str = str(abs(winnings))
        w_str = ''.join([x if int(x) % 2 == 0 else str((int(x) - 1) % 10) for x in w_str])
        w = int(w_str)
        if winnings < 0:
            w = -w
        winnings = w
    elif o == 'REVERSERSIFFER':
        w = int(str(abs(winnings))[::-1])
        if winnings < 0:
            w = -w
        winnings = w
    elif 'OPP' in o:
        num = int(o.split('OPP')[1])
        while str(winnings)[len(str(winnings)) - 1] != '7':
            winnings += 1
    elif o == 'GANGEMSD':
        winnings = winnings * int(str(abs(winnings))[0])
    elif o == 'DELEMSD':
        winnings = int(winnings / int(str(abs(winnings))[0]))
    elif 'ROTER' in o:
        if 'PAR' in o:
            for i in range(0, wheel_states.shape[0], 2):
                wheel_states[i] = np.roll(wheel_states[i], -1)
        elif 'ODDE' in o:
            for i in range(1, wheel_states.shape[0], 2):
                wheel_states[i] = np.roll(wheel_states[i], -1)
        elif 'ALLE' in o:
            for i in range(0, wheel_states.shape[0]):
                wheel_states[i] = np.roll(wheel_states[i], -1)
        else:
            raise Exception("Faulty rotatation call.")
    else:
        raise Exception(f"Encountered an unexpected operation: {o}")
    wheel_states[index] = np.roll(wheel_states[index], -1)
    return play(wheel_states, winnings)


coins = grand_prize = -1
original_copy = np.copy(original_wheels)

for i in range(1, 11):
    winnings = play(np.copy(original_wheels), i)
    print(f"{i} mynter: {winnings}")
    if winnings > grand_prize:
        coins = i
        grand_prize = winnings

    # Ensure integrity of original wheel states
    if original_wheels.all() != original_copy.all():
        raise Exception("Original wheel states have been compromized.")
print(f"Høgaster gevinst med {coins} mynt(er): {grand_prize}")
