lista = input() .split()

h1 = int(lista[0])
h2 = int(lista[1])

hf = 0

if h1 < h2:
  hf = h2 - h1
  print(f'O JOGO DUROU {hf} HORA(S)')

else:
  hf = (24 - h1) + h2
  print(f'O JOGO DUROU {hf} HORA(S)')

