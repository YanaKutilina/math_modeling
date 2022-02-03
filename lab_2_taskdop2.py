a = int(input("Введите первый отрезок= "))
b = int(input("Введите второй отрезок= "))
c = int(input("Введите третий отрезок= "))
if a + b <= c or a + c <= b or b + c <= a:
  print("Треугольник не существует")
elif a != b and a != c and b != c:
  print("Разносторонний")
elif a == b == c:
  print("Равносторонний")
else:
  print("Равнобедренный")