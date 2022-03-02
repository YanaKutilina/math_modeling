a=int(input("ВВедите число: "))
for i in range(1,a+1):
  if a%i==0:
    for l in range(2,i+1):
      if i%l==0:
        break
print(l)