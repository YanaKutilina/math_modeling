def my_func(a,b):
  x=3*a-b
  return x

#tmp=my_fenc() ошибка нет аргуметов

def my_func(a=1,b=0):
  x=3*a-b
  return x
print(my_func())

print(my_func())
print(my_func(3, 4))
print(my_func(3))
print(my_func(b=3))
print(my_func(b=3, a=9))

# Так НЕЛЬЗЯ!
# def my_func(a=0, b):
#     x = 3 * a - b
#     return x

#картедж
def my_func(*args):
    x = 3 * args[0] - args[1]
    return x

print(my_func(3, 4))
print(my_func(3, 4, 8))

#словарь
def my_func(**kwrgs):
    x = 3 * kwrgs['obj_1'] - kwrgs['obj_2']
    return x
print(my_func(obj_1=3, obj_2=4))

  