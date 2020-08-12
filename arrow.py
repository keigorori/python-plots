# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import SubplotZero

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
    # 余白
    fig.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95)

    # 枠線を非表示
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    # 軸をゼロ中心へ移動
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))

    # 軸矢印
    ax.axis[:].set_visible(False)
    for direction in ["xzero", "yzero"]:
        ax.axis[direction].set_visible(True)
        ax.axis[direction].set_axisline_style("->", size=2.0)
        ax.axis[direction].toggle(all=False)

    # 背景透明
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)


def plot_arrow(ax, x, y, sampling_period):
    """
    矢印列をプロット
    Parameters
    ----------
    ax : Axes
        対象のAxes
    x : ndarray
        xデータ
    y : ndarray
        yデータ
    sampling_period : int
        サンプリング周期
    """
    # ゼロに最も近いインデックス
    zero_idx = np.abs(np.asarray(x)).argmin()
    offset = zero_idx % sampling_period

    x_sampl = x[offset::sampling_period]
    y_sampl = y[offset::sampling_period]

    # 矢印の描画
    # ここではquiverを使う
    for i in range(0, len(x_sampl)):
        ax.quiver(x_sampl[i], 0, 0, y_sampl[i], width=0.005, headwidth=5, color="blue", scale=1, scale_units="xy")




def main():
    # データ
    x = np.arange(-5, 5, 1)
    y = [1.0]*1000

    # プロット
    fig = plt.figure()
    ax = SubplotZero(fig, 111)
    fig.add_subplot(ax)
    plot_arrow(ax, x, y, 1)

    # 表示設定
    margin = 0.5
    set_display(fig, ax)
    ax.set_xlim(x[0]-margin, x[-1]+margin)
    ax.set_ylim(-0.2, 1.5)

    # ファイル保存
    fig.savefig("arrow.png")

    # 表示
    plt.show()


if __name__ == '__main__':
    main()