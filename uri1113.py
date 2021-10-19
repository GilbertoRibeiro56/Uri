while True:
  lista = input().split()
  x = int(lista[0])
  y = int(lista[1])
  
  if x > y:
    print('Decrescente')
    
  if x < y:
    print('Crescente')
    
  if x == y:
    break