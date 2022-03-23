import numpy as np

N=int(input('N = '))
M=int(input('M = '))

L=np.zeros((N, M))

for i in range(N):
  for j in range(M):
    if (np.sin(N*(i+1)+M*(j+1)))>0:
      L[i, j]=np.sin(N*(i+1)+M*(j+1))
    else:
      L[i, j]=0
print(L)

a=int(input())
b=int(input())
for i in range(N):
  L[i,a],L[i,b]=a[i,b],a[i,a]
  print(L[i])



