import matplotlib.pyplot as plt
import numpy as np



def gip(k=1,a=1,title='Giperbola plotter'):
  x=np.arange(-10,10,0.01)
  
  plt.plot(x,y,label='my Giperbola')
  plt.title(title)
  plt.legend()
  plt.show()
gip()
  