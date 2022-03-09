import numpy as np
x0=0
y0=0
vx=3
vy=5
g=9.8
t=np.arange(0,5,0.1)
x=x0+vx*t
y=y0+vy*t-g*t**2/2

coords=np.zeros((len(t),3))
for i in range(len(t)):
  coords[i,0]=t[i]
  coords[i,1]=x[i]
  coords[i,2]=y[i]

print(coords)