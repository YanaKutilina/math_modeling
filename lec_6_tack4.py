import numpy as np
import matplotlib.pyplot as plt

phi0 = 0.01
phi1 = 8 * np.pi
N = 100

phi = np.linspace(phi0, phi1, N)

################# Логарифмическая спираль #################
b = 0.02
r = exp(b * phi)

x = []
y = []

for i in range(N):
    x.append(r[i]*np.cos(phi[i]))
    y.append(r[i]*np.sin(phi[i]))

fig = plt.figure(figsize=(8,8), facecolor='pink', frameon=True)
plt.plot(x,y)
plt.minorticks_on()
plt.grid(which='major',linewidth = 2)
plt.grid(which='minor')
plt.savefig('results/Log_spiral.png')

################## Архимедова спираль #################
k = 0.5
r2 = k * phi

x = []
y = []

for i in range(N):
    x.append(r2[i]*np.cos(phi[i]))
    y.append(r2[i]*np.sin(phi[i]))

fig = plt.figure(figsize=(8,8), facecolor='pink', frameon=True)
plt.plot(x,y)
plt.minorticks_on()
plt.grid(which='major',linewidth = 2)
plt.grid(which='minor')
plt.show()
plt.axis('equal')
plt.savefig('Arch_spiral.png')

################## Спираль жезл #################
k = 0.2
r3 = k / np.sqrt(phi)

x = []
y = []

for i in range(N):
    x.append(r3[i]*np.cos(phi[i]))
    y.append(r3[i]*np.sin(phi[i]))

fig = plt.figure(figsize=(8,8), facecolor='pink', frameon=True)
plt.plot(x,y)
plt.minorticks_on()
plt.grid(which='major',linewidth = 2)
plt.grid(which='minor')
plt.show()
plt.savefig('Zhezl_spiral.png')

################## Роза #################
k = 3 / 2
r4 = np.sin(k * phi)

x = []
y = []

for i in range(N):
    x.append(r4[i]*np.cos(phi[i]))
    y.append(r4[i]*np.sin(phi[i]))

fig = plt.figure(figsize=(8,8), facecolor='pink', frameon=True)
plt.plot(x,y)
plt.minorticks_on()
plt.grid(which='major',linewidth = 2)
plt.grid(which='minor')
plt.show()
plt.savefig('Rose.png')