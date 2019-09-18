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
    ax.set_xlabel("trials [times]")
    ax.set_ylabel("distance [m]")

    # 目盛間隔
    ax.set_xticks(np.arange(0,50, 5))
    ax.set_yticks(np.arange(0,105, 5))

    # 背景透明
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)


def plot_series(ax, trials,  begin, end, step, marker_begin, marker_end):
    y = np.arange(begin, end, step)
    x = np.arange(trials, trials+len(y), dtype="int")
    ax.scatter(x, y, marker=marker_begin, color="royalblue")
    ax.scatter(trials+len(y), end, marker=marker_end, color="royalblue")
    return len(y) + 1


def main():
    # データ
    trials = 1
    step = 5

    # プロット
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    trials += plot_series(ax, trials, 5, 45, step, "x", "o")
    trials += plot_series(ax, trials, 100, 30, -step, "o", "x")
    trials += plot_series(ax, trials, 5, 40, step, "x", "o")
    trials += plot_series(ax, trials, 100, 30, -step, "o", "x")

    # 表示設定
    set_display(fig, ax)

    # ファイル保存
    fig.savefig("trials.png")

    # 表示
    plt.show()


if __name__ == '__main__':
    main()