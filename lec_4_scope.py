
x0 = 10 
def move(t):
    x = x0 * t
    return x
  #или 
  # x=локальная print(x) нельзя
  #t=глобальная

print(move(3))

def my_func():
  global a
  a = 'Bad'
  print(a)
#глобальной переменной присваевается новое значение
my_func()
print(a)