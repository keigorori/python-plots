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
    # 枠線を非表示
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    # 表示範囲
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 105)

    # ラベル
    ax.set_xlabel("trial [times]")
    ax.set_ylabel("distance [m]")

    # 目盛間隔
    ax.set_xticks(np.arange(0,50, 5))
    ax.set_yticks(np.arange(0,105, 5))

    # 背景透明
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)


def main():
    # データ
    trial = 1
    step = 5

    y1 = np.arange(5, 40, step)
    x1 = np.arange(trial, trial+len(y1), dtype="int")
    trial += len(y1)

    y2 = np.arange(100, 30, -step)
    x2 = np.arange(trial, trial+len(y2), dtype="int")
    trial += len(y2) 

    y3 = np.arange(5, 45, step)
    x3 = np.arange(trial, trial+len(y3), dtype="int")
    trial += len(y3)

    y4 = np.arange(100, 25, -step)
    x4 = np.arange(trial, trial+len(y4), dtype="int")
    trial += len(y4) 


    # プロット
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.scatter(x1, y1, marker="o", color="royalblue")
    ax.scatter(x2, y2, marker="x", color="royalblue")
    ax.scatter(x3, y3, marker="o", color="royalblue")
    ax.scatter(x4, y4, marker="x", color="royalblue")

    # 表示設定
    set_display(fig, ax)

    # ファイル保存
    fig.savefig("trials.png")

    # 表示
    plt.show()


if __name__ == '__main__':
    main()