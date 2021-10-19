n = int(input())
c = 1
divisao = 0
while c <= n:
  c +=1
  lista = input() .split()
  x = int(lista[0])
  y = int(lista[1])

  if y == 0:
    print('divisao impossivel')
  
  if y != 0:
    divisao = x / y
    print(f'{divisao:.1f}')
