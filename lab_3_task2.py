import numpy as np
import lab_3_task1 as pc

H = 100
a = np.pi / 3
b = 30

v = np.sqrt(pc.Free_fall * H * (np.tan(b)**2 / 2 * np.cos(a)**2 * (1 - np.tan(b) * np.tan(a))))
print(v)

T = 200
E = 300

N = 2 / np.pi * pc.hight / (pc.kar * T)*(3 / 2) * pc.ed*(-E / pc.kar * T) * E**(T / 2)
print(N)