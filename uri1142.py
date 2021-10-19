x = int(input())
c = 0
i = 1
y = (x * 4)
while c <= x:
  while i <= y:
    if i % 4 == 0:
      print('PUM')
      i += 1
    else:
      print(i, end= ' ')
      i += 1

  c +=1
