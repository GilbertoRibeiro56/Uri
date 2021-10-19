n = int(input())
c = 1
while c <= n:
  x = int(input())

  if (x > 0) and (x % 2 == 0):
    print('EVEN POSITIVE')

  if (x > 0) and (x % 2 == 1):
    print('ODD POSITIVE')

  if (x < 0) and (x % 2 == 0):
    print('EVEN NEGATIVE')

  if (x < 0) and (x % 2 == 1):
    print('ODD NEGATIVE')

  if (x == 0):
    print('NULL')

  c += 1
