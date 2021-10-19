c = 0
p = 0
n = 0
while True:
  x = float(input())

  if x > 0:
    p += 1
    n += x
  
  c += 1
  if c == 6:
    break

media =  n / p
print(f'{p} valores positivos')
print(f'{media:.1f}')


