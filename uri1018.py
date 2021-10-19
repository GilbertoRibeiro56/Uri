n = int(input())
print(n)

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

  


print(cedula100,'nota(s) de R$ 100,00')
print(cedula50,'nota(s) de R$ 50,00')
print(cedula20,'nota(s) de R$ 20,00')
print(cedula10,'nota(s) de R$ 10,00')
print(cedula5,'nota(s) de R$ 5,00')
print(cedula2,'nota(s) de R$ 2,00')
print(cedula1,'nota(s) de R$ 1,00')
