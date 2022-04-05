figura=int(input("Введите название фигуры 1= круг,2=прямоугольник,3=треугольник: "))

def crug(radius):
  ploshad=3.14*radius**2
  return ploshad
def pryam(a,b):
  ploshad=a*b
  return ploshad 
def treu(a,b):
  ploshad=a*b/2
  return ploshad 
if figura==1:
  radius=int(input("Введите радиус окружности: "))
  print(crug(radius))
elif figura==2:
  a=int(input("Введите значение длины: "))
  b=int(input("Введие значение ширины: "))
  print(pryam(a,b))
else:
  a=int(input("Введите значение основания: "))
  b=int(input("Введите значенте высоты: "))
  print(treu(a,b))
  