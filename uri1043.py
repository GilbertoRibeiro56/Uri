lista = input() .split()

a = float(lista[0])
b = float(lista[1])
c = float(lista[2])


if abs(b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
  p = a + b + c
  print(f'Perimetro = {p:.1f}')

else:
  a = ((a + b) * c) / 2
  print(f'Area = {a:.1f}')
   
