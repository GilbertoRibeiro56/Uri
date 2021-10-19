import math

lista = input() .split()
a = int(lista[0])
b = int(lista[1])
c = int(lista[2])

MaiorAB = (a + b + abs (a - b))/2

resultado = MaiorAB + c + abs (MaiorAB - c)/2

print("%d eh o maior" %resultado)
