win_gre = 0
win_int = 0
draw = 0

while True:
  gol = input() .split()
  gol_int = int(gol[0])
  gol_gre = int(gol[1])

  if gol_int == gol_gre:
    draw += 1
    
  else:
    if gol_int < gol_gre:
      win_gre += 1

    else:
      win_int += 1

  print('Novo grenal (1-sim 2-nao)')
  escolha = int(input())

  if escolha == 2:
    break

jogos = win_gre + win_int + draw
print(f'{jogos} grenais')
print(f'Inter:{win_int}')
print(f'Gremio:{win_gre}')
print(f'Empates:{draw}')

if win_gre > win_int:
  print('Gremio venceu mais')

if win_gre < win_int:
  print('Inter venceu mais')

else:
  print('Nao houve vencedor')
