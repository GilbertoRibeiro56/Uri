md = 0.0
while True:
  x = float(input())
  if (x < 0) or (x > 10):
    print('nota invalida')

  else:
    md += x
    break
while True:
  y = float(input())
  if (y < 0) or (y > 10):
    print('nota invalida')

  else:
    md += y
    break

md /= 2
print(f'media = {md:.2f}')
