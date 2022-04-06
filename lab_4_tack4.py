import numpy as np

def y_x(a,b,N):
  x=np.linspace(a,b,N)
  y=x**2
  return y

print(y_x(-5,5,20))