n = int(input())
c = 1
pot = 0
while c <= n:
  if c % 2 == 0:
    pot = c ** 2
    print(f'{c}^{2} = {pot}')

  c += 1
