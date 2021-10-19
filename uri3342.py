n = int(input())
casas = n**2
branca = 0
preta = 0

if casas % 2 == 1:
  branca = (casas // 2) + 1
  preta = casas // 2

  print(f'{branca} casas brancas e {preta} casas pretas')

else:
  branca = casas // 2
  preta = casas // 2

  print(f'{branca} casas brancas e {preta} casas pretas')
