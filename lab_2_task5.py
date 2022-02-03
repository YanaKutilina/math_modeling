a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
if a%b == 0:
    print(a,"делится на",b)
else:
    print(a,"не делится на",b)
    print("Остаток: " ,a%b)
print("Частное: ",a//b)