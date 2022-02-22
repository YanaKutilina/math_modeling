a = int(input('Введите число: '))
f1 = f2 = 1

print(f1, f2, end=' ')
 
for i in range(2, a+1):
    f1, f2 = f2, f1 + f2
    print(f2, end = ' ')
