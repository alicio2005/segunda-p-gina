"""def increment(x):
    return x + 2

def increment1(a, funcion, b):
    return a + funcion(b)

resultado = increment1(2, increment, 5)
print(resultado)"""
"""
def suma(a):
    return a + 5

def increment(x, f):
    return x + f(x)
resultado = increment(5, suma)
print(resultado)"""

"""v = lambda a, b : a + b
print(v(3, 4))"""

"""c1 = {'1', 2, 3, 4, 5, 5, 4, 3, 2, '1', 0}
print(c1)"""

#c1 = {'a', 'b', 'c'}
#c2 = {'d', 'f', 'g', 'c', 'a'}


"""c1.symmetric_difference(c2)
print(c1)"""

"""print(c1.union(c2))"""

"""c1.difference_update(c2)
print(c1)

c3 = c1.difference(c2)
print(c3)"""

"""c1.discard('a')
print(c1)"""

"""c1.intersection_update(c2)
print(c1)

c3 = c1.intersection(c2)
print(c3)"""

"""numbers = [1, 2, 3, 4, 5]
numbers_v1 = []
for i in numbers:
    numbers_v1.append(i * 2)

print(numbers_v1)

v3 = list(map(lambda i:i*2, numbers))
print(v3)

numbers_2 = [6, 7, 8, 9, 10]"""

"""numbers_v1 = [1, 2, 3, 4, 5]
resultado = list(map(lambda a: a * 2, numbers_v1))
print(resultado)

numbers_v2 = [6, 7, 8, 9, 10]
resultado_1 = list(map(lambda a, b : a + b, numbers_v1, numbers_v2))
print(resultado_1)"""

"""numbers1 = [1, 2, 3, 4, 5]
numbers2 = [6, 7, 8, 9, 10]

resultados = list(map(lambda  a, b : a * b, numbers1, numbers2))
print(resultados)

def increment1(x):
    return x + 6

def increment2(x, función):
    return x + función(x)
resultado = increment2(5, increment1)

print(resultado)

print(numbers1)"""


"""number = [1, 2, 3, 4, 5]

resultado = list(map(lambda a : a * 4, number))
print(resultado)"""

number = [
    {'nombre': 'Playera', 'precio': 100},
    {'nombre': 'Pantalon', 'precio': 150},
    {'nombre': 'sueter', 'precio': 200},
    {'nombre': 'zapatos', 'precio': 250}
]

resultado = list(map(lambda a : a["precio"], number))
print(resultado)