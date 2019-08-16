# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def set_transparency(target):
    """
    対象の背景を透明にする
    Parameters
    ----------
    target : Figure or Axes
        背景を透明にしたい対象
    """
    # パッチのアルファを0にする
    target.patch.set_alpha(0.0)


def main():
    # データ
    x = np.linspace(0, 50, 1000)
    y = np.sin(x)

    # プロット
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(x,y)

    # 表示設定
    set_transparency(fig)
    set_transparency(ax)

    # ファイル保存
    fig.savefig("transparency.png")

    # 表示
    plt.show()


if __name__ == '__main__':
    main()