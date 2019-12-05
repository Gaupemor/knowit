import re
import numpy as np

"""
Luke 5: Ønskerøre
https://julekalender.knowit.no/doors/ck3r9wecdbu640109c9lkl93c
"""

lista = "tMlsioaplnKlflgiruKanliaebeLlkslikkpnerikTasatamkDpsdakeraBeIdaegptnuaKtmteorpuTaTtbtsesOHXxonibmksekaaoaKtrssegnveinRedlkkkroeekVtkekymmlooLnanoKtlstoepHrpeutdynfSneloietbol"

# Oppskrfita baklengs

# 3

temp = re.findall('...', lista)

for i in range(len(temp) // 2):
    from_1 = temp[i]
    from_2 = temp[len(temp) - 1 -i]

    temp[len(temp) - 1 - i] = from_1
    temp[i] = from_2

lista = ''.join([str(t) for t in temp])

# 2

temp_string = np.array(list(lista))
i = temp_string.shape[0] - 1
while i > 0:
    from_right = temp_string[i]
    from_left = temp_string[i - 1]

    temp_string[i] = from_left
    temp_string[i - 1] = from_right

    i -= 2

lista = ''.join([str(elem) for elem in temp_string])

# 1
lista = lista[len(lista) // 2:] + lista[:len(lista) // 2]

print(lista)
