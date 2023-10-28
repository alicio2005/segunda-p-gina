"""lista = []

for i in range(0, 10):
    lista.append(i * 4)

print(lista)"""

import random 
nombre = ['miguél', 'juan', 'sergio', 'daniel']

items = {p:random.randint(0, 10) for p in nombre}
print(items)

item_v2 = {pv2:r for pv2, r in items if r > 2}
print(item_v2)