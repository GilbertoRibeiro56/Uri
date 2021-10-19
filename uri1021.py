n = float(input())

cedula100 = n // 100
n = n - cedula100 * 100

cedula50 = n // 50
n = n - cedula50 * 50

cedula20 = n // 20
n = n - cedula20 * 20

cedula10 = n // 10
n = n - cedula10 * 10

cedula5 = n // 5
n = n - cedula5 * 5

cedula2 = n // 2
n = n - cedula2 * 2

cedula1 = n // 1
n = n - cedula1 * 1

moeda1 = n // 0.5
n = n - moeda1 * 0.5

moeda2 = n // 0.25
n = n - moeda2 * 0.25

moeda3 = n // 0.10
n = n - moeda3 * 0.10

moeda4 = n // 0.05
n = n - moeda4 * 0.05

moeda5 = n // 0.01

print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(int(cedula100)))
print('{} nota(s) de R$ 50.00'.format(int(cedula50)))
print('{} nota(s) de R$ 20.00'.format(int(cedula20)))
print('{} nota(s) de R$ 10.00'.format(int(cedula10)))
print('{} nota(s) de R$ 5.00'.format(int(cedula5)))
print('{} nota(s) de R$ 2.00'.format(int(cedula2)))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(int(cedula1)))
print('{} moeda(s) de R$ 0.50'.format(int(moeda1)))
print('{} moeda(s) de R$ 0.25'.format(int(moeda2)))
print('{} moeda(s) de R$ 0.10'.format(int(moeda3)))
print('{} moeda(s) de R$ 0.05'.format(int(moeda4)))
print('{} moeda(s) de R$ 0.01'.format(int(moeda5)))
