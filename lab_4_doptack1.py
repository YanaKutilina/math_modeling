def sub(a,n):
  b=a
  while n>1:
    a*=b
    n-=1
  print(a)
a=int(input())
n=int(input())
sub(a,n)