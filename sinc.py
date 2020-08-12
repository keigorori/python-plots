# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def set_display(fig, ax):
    """
    表示周りの設定
    Parameters
    ----------
    fig : Figure
        対象のFigure
    ax : Axes
        対象のAxes
   """
    # 余白をゼロにする
    fig.subplots_adjust(left=0.0, bottom=0.0, right=1.0, top=1.0)

    # 枠線を非表示
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    # 軸をゼロ中心へ移動
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))

    # 目盛りを表示
    ax.tick_params(left=False, bottom=True, right=False, top=False)
    ax.set_xticks([-4*np.pi, -3*np.pi, -2*np.pi, -1*np.pi, 0, 1*np.pi, 2*np.pi, 3*np.pi, 4*np.pi])
    ax.set_yticks([0.5, 1.0])

    # 目盛りラベルを表示
    ax.tick_params(labelleft=True, labelbottom=True, labelright=False, labeltop=False)
    ax.set_xticklabels(["-4π", "-3π", "-2π", "-π", "0", "π", "2π", "3π", "4π"])

    # 背景透明
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)



def sinc(x):
    return np.sin(x)/x

def main():
    # データ
    x = np.linspace(-4*np.pi, 4*np.pi, 1000)
    coef = 1/(2*sinc(0.5*np.pi))
    y_0 = sinc(x)
    y_1 = sinc(x+0.5*np.pi) * coef
    y_2 = sinc(x-0.5*np.pi) * coef
    y_3 = y_1 + y_2


    # プロット
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    ax.plot(x, y_0,)
    ax.plot(x, y_1, linestyle="dashed", linewidth=0.5)
    ax.plot(x, y_2, linestyle="dashed", linewidth=0.5)
    ax.plot(x, y_3,)

    # 表示設定
    set_display(fig, ax)
    ax.set_xlim(x[1], x[-1])

    # ファイル保存
    fig.savefig("sinc.png")

    # 表示
    plt.show()


if __name__ == '__main__':
    main()