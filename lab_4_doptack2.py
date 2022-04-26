def fib(n):
  f1 =0
  f2 = 1
  n = int(n) - 2
  while n > 0:
    f1, f2 = f2, f1 + f2
    n -= 1
  print(f2)
n = int(input('Введите число: '))
fib(n)