import numpy as np
b = np.arange(1, 6, 1)
print(b)
def funs():
  s=1
  for i in range(len(b)):
    s=s*b[i]
  return s

print(funs())




