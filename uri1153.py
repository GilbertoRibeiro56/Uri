numero = int(input())
i = 1

while i <= numero:
  num = i
  i += 1
  
  fat = 1
  if num > 1:
    c = 1
    while c <= num:
      fat *= c
      c += 1
  
print(fat)



