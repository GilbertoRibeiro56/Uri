x = int(input())
c = 1

while c <= x:
  print(c, end=" ")
  print(c**2, end=" ")
  print(c**3, end="\n")
  print(c, end=" ")
  print((c**2)+1, end=" ")
  print((c**3)+1, end="\n")

  c += 1
