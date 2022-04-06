import matplotlib.pyplot as plt
import numpy as np
# не можеи явным образом выразить y через x или наоборот 
def circle_plotter(a=5,b=9):
  x=np.arange(-2*radius, 2*radius, 0.1)
  y=np.arange(-2*radius, 2*radius, 0.1)

  x,y=np.meshgrid(x,y)# делает массив для каждого x свои y
  fxy = (x**2/a**2)+(y**2/b**2)=1
  plt.contour(x, y, fxy, levels=[0])
  plt.axis('equal') # когда не велирует маштабируемом(маштаб фигуры)
  plt.show()
  
circle_plotter()