c = 1
par = 0
impar = 0
positivo = 0
negativo = 0
while c <= 5:
  x = int(input())

  if x > 0:
    positivo += 1

  if x < 0:
    negativo += 1

  if x % 2 == 0:
    par += 1

  if x % 2 == 1:
    impar += 1

  c += 1 

print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')
    
