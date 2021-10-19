lista = input().split()
E = int(lista[0])
F = int(lista[1])
C = int(lista[2])
X = E+F
cont = 0
if E>=0 or F >= 0 or C >= 0:
  if 1<C<2000 or F>1000 or E>1000:
    while X >= C:
      X-=C
      X+=1
      cont +=1
    print(f'{cont:.0f}')
