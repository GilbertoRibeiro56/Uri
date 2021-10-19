dia1 = input() .split()

dia_txt = (dia1[0])
dia_num = int(dia1[1])

hora1 = input().split(':')
hor1 = int(hora1[0])
min1 = int(hora1[1])
seg1 = int(hora1[2])

dia2 = input() .split()

dia_txt2 = (dia2[0])
dia_num2 = int(dia2[1])

hora2 = input().split(':')
hor2 = int(hora2[0])
min2 = int(hora2[1])
seg2 = int(hora2[2])

minuto_seg = 60
hora_seg = minuto_seg * 60
dia_seg = hora_seg * 24

ini = seg1 + min1 * minuto_seg + hor1 * hora_seg + dia_num * dia_seg
end = seg2 + min2 * minuto_seg + hor2 * hora_seg + dia_num2 * dia_seg

if ini < end:
  tempo = end - ini
  dias = int(tempo/dia_seg)
  tempo = tempo%dia_seg
  horas = int(tempo/hora_seg)
  tempo = tempo%hora_seg
  minutos = int(tempo/minuto_seg)
  tempo = tempo%minuto_seg
  segundos = tempo
  print(f'{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)')

