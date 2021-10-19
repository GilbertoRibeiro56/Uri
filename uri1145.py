lista = input() .split()
x = int(lista[0])
y = int(lista[1])
c = 1

while c <= y:
  print(c, end=' ')
  c += 1
  if c % x == 0:
    print(c, end='\n')
    c += 1
