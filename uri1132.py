x = int(input())
y = int(input())
c = 0

if x > y:
  menor = y
  maior = x

if x <= y:
  menor = x
  maior = y
  
while menor <= maior:
  if menor % 13 != 0:
    c += menor
  menor += 1
print(c)
  
