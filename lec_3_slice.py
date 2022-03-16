a=[4,16,10,5,7,1,8]
slice = a [2:5:1]
print(slice)

import numpy as np

a=[1,5,3,6]
slice = a[0:2:1]
print(slice)

slice=a[::-1]
print(slice)

b=np.array([a,np.array(a)*3])
print(b)

#срезать столбец
slice=b[::,-1]
print(slice)

slice=b[::,1:3]
print(slice)

slice=b[::,1::]
print(slice)


slice=b[0:2,1:3] #строка столбец
print(slice)
