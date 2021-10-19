c = 0
par = 0
while True:
  x = int(input())

  if x % 2 == 0:
     par += 1
      
  c += 1
  if c >= 5:
    break

print(f'{par} valores pares')


