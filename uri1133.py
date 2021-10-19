x = int(input())
y = int(input())
c = 0

if x > y:
  menor = y
  maior = x

if x <= y:
  menor = x
  maior = y

menor += 1  
while menor < maior:
  if (menor % 5 == 2) or (menor % 5 == 3):
    print(menor)

  menor += 1
  
