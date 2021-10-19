idade = int(input())

ano = idade // 365
idade = idade - ano * 365

mes = idade // 30
idade = idade - mes * 30

print(ano,'ano(s)')
print(mes,'mes(es)')
print(idade,'dia(s)')
