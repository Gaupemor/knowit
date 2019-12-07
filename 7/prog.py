"""
Luke 7: Hvelvets diskrete kode
https://julekalender.knowit.no/doors/ck3ukyvpocn0f0109cxuw21ht
"""

base = 5897
safe_num = 27644437

def special_div(x):
    # a
    y = 0
    for y_ in range(2, safe_num):
         b = y_ * x
         r = b % safe_num
         if r == 1.0:
             y = y_
             break
    # b
    z = base * y
    # c
    return z % safe_num

print(special_div(7))
