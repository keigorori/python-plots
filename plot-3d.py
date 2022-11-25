# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def main():
    x = np.linspace(-10, 10, 512)
    y = np.linspace(-10, 10, 512)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x**2+y**2)) / np.sqrt(x**2+y**2)

    # plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_wireframe(x, y, z)
    plt.show()


if __name__ == '__main__':
    main()
