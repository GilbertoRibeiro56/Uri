x = int(input())
c = 1
dentro = 0
fora = 0


while c <= x:
  n = int(input())
  if (n >= 10) and (n <= 20):
    dentro += 1

  else:
    fora += 1

  c += 1

print(f'{dentro} in')
print(f'{fora} out')