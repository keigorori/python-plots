# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def main():
    x = np.linspace(0, 50, 1000)
    y = np.sin(x)
    plt.plot(x,y)

    plt.show()

if __name__ == '__main__':
    main()