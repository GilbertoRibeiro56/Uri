a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

p = 0
i = 0
po = 0
n = 0
v0 = 0


if (a % 2 == 0):
  p += 1

else:
  i += 1

if (a > 0):
  po += 1

elif a == 0:
  v0 = 0

else:
  n = n + 1

if (b % 2 == 0):
  p = p + 1

else:
  i = i + 1

if (b > 0):
  po = po + 1

elif b == 0:
  v0 = 0

else:
  n = n + 1

if (c % 2 == 0):
  p = p + 1

else:
  i = i + 1

if (c > 0):
  po = po + 1

elif c == 0:
  v0 = 0

else:
  n = n + 1

if (d % 2 == 0):
  p = p + 1

else:
  i = i + 1

if (d > 0):
  po = po + 1

elif d == 0:
  v0 = 0

else:
  n = n + 1

if (e % 2 == 0):
  p = p + 1

else:
  i = i + 1

if (e > 0):
  po = po + 1

elif e == 0:
  v0 = 0

else:
  n = n + 1


print(p,'valor(es) par(es)')
print(i,'valor(es) impar(es)')
print(po,'valor(es) positivo(s)')
print(n,'valor(es) negativo(s)')
