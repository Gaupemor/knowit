import numpy as np
import urllib.request
from PIL import Image

"""
Luke 3: Flate pakker er også pakker
https://julekalender.knowit.no/doors/ck3naau5qaza901092kpj4a40
"""

input_file = (
    urllib.request
    .urlopen("https://knowit-julekalender.s3.eu-central-1.amazonaws.com/2019-luke3/img.txt")
    )
# Denne operasjonen tek ei stund
flat_image = np.genfromtxt(input_file , delimiter=1)

cmap = {0: (255,255,255),
        1: (0,0,0)}

# Fant dimensjonane manuelt
d = [1287, 560]

data = [cmap[digit] for digit in flat_image]
img = Image.new('RGB', (d[0], d[1]), "white")
img.putdata(data)
img.show()
