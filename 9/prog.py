import numpy as np
import urllib.request

"""
Luke 9: Krampustall
https://julekalender.knowit.no/doors/ck3vosq73cw370109qnk7nu17
"""

input_file = (
    urllib.request
    .urlopen("https://julekalender.knowit.no/resources/2019-luke09/krampus.txt")
    )
nums = np.loadtxt(input_file, dtype=np.int64)

sum = 0

for n in nums:
    pow = n*n

    p_str = str(pow)
    for i in range(1, len(p_str)):
        a = int(p_str[:i])
        b = int(p_str[i:])
        if a + b == n and a != 0 and b != 0:
            sum += n
            continue

print(sum)
