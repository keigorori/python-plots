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

    # 目盛りを非表示
    ax.tick_params(left=False, bottom=False, right=False, top=False)

    # 目盛りラベルを非表示
    ax.tick_params(labelleft=False, labelbottom=False, labelright=False, labeltop=False)

    # 背景透明
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)


def plot_sampling(ax, x, y, sampling_period, is_half=False):
    """
    データのサンプリングをプロット
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
    is_half : bool
        ゼロ起点から半サンプルずらす
    """
    # ゼロに最も近いインデックス
    zero_idx = np.abs(np.asarray(x)).argmin()
    offset = zero_idx % sampling_period

    # 半サンプリング周期ずれた位置からサンプリング
    if is_half:
        offset += int(sampling_period/2)

    x_sampl = x[offset::sampling_period]
    y_sampl = y[offset::sampling_period]

    # 補助線の描画
    for i in range(0, len(x_sampl)):
        ax.vlines(x=x_sampl[i], ymin=min(0, y_sampl[i]), ymax=max(0, y_sampl[i]), colors="gray", linewidth=1.0)

    # 散布図としてマーカーをプロット
    ax.scatter(x_sampl, y_sampl, marker="o")



def main():
    # データ
    x = np.linspace(-np.pi, 4*np.pi, 1000)
    y = np.sin(x)

    # プロット
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    plot_sampling(ax, x, y, 30)
    ax.plot(x, y, linestyle="dashed")

    # 表示設定
    set_display(fig, ax)
    ax.set_xlim(x[1], x[-1])

    # ファイル保存
    fig.savefig("sampling.png")

    # 表示
    plt.show()


if __name__ == '__main__':
    main()