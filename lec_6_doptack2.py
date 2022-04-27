import numpy as np
import matplotlib.pyplot as plt

def cone(p, epsilon):
    phi = np.linspace(0, 2*np.pi, 100)
    r = 1 + epsilon * np.cos(phi)
    x = r * np.cos(phi)
    y = r * np.sin(phi)

    # fig = plt.figure(figsize=(8,8), facecolor='pink', frameon=True)
    plt.plot(x,y)
    # plt.minorticks_on()
    # plt.grid(which='major',linewidth = 2)
    # plt.grid(which='minor')
    # plt.axis('equal')

    plt.show()
    # plt.savefig('pic_ellipsw')


cone(1, 0.4)