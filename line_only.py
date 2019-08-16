# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def set_display(fig, ax):
    """
    表示周りの設定
    Parameters
    ----------
    target : Figure
        対象のFigure
    """
    # 余白をゼロにする
    fig.subplots_adjust(left=0.0, bottom=0.0, right=1.0, top=1.0)

    # 枠線を非表示
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    # 目盛りを非表示
    ax.tick_params(left=False, bottom=False, right=False, top=False)

    # 目盛りラベルを非表示
    ax.tick_params(labelleft=False, labelbottom=False, labelright=False, labeltop=False)

    # 背景透明
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)


def main():
    # データ
    x = np.linspace(0, 2*np.pi, 1000)
    y = np.sin(x)

    # プロット
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(x,y)

    # 表示設定
    set_display(fig, ax)
    ax.set_xlim(0, (1000-1)*2*np.pi/1000)

    # ファイル保存
    fig.savefig("line-only.png")

    # 表示
    plt.show()


if __name__ == '__main__':
    main()