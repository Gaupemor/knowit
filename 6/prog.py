import numpy as np
import urllib.request
import cv2

"""
Luke 6: Birte sin brilliante biletebeskyttelse
https://julekalender.knowit.no/doors/ck3r9zcm6bu7d0109solzlvjy
"""

input_file = (
    urllib.request
    .urlopen("https://knowit-julekalender.s3.eu-central-1.amazonaws.com/2019-luke6/mush.png")
    )
img = cv2.imdecode(np.asarray(bytearray(input_file.read()), dtype=np.uint8), -1)

for i in range(img.shape[0] - 1, -1, -1):
    for j in range(img.shape[1] - 1, -1, -1):
        xor_result = cv2.bitwise_xor(img[i, j], img[i, j - 1])
        xor_result = np.array([xor_result[0][0], xor_result[1][0], xor_result[2][0]])
        img[i, j] = xor_result

cv2.imshow("Luke 6", img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
