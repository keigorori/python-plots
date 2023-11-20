# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import FancyArrowPatch


class Arrow3D(FancyArrowPatch):
    # quiverだと3D表示が見づらいのでFancyArrowPatchで3D空間に2D表示を行う
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)


def main():
    # プロット設定
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    # 余白を無くす
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    # 平行投影
    ax.set_proj_type("ortho")

    # 背面グリッド
    # 背面を消す
    ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    # グリッド
    ax.xaxis._axinfo["grid"]["color"] = "lightgray"
    ax.yaxis._axinfo["grid"]["color"] = "lightgray"
    ax.zaxis._axinfo["grid"]["color"] = "lightgray"

    # 目盛
    # グリッド用に値は設定しておく
    ax.set_xticks(np.arange(0.1, 1.1, 0.1))
    ax.set_yticks(np.arange(0.1, 1.1, 0.1))
    ax.set_zticks(np.arange(0.1, 1.1, 0.1))
    # 目盛ラベルを消す
    ax.tick_params(labelbottom=False, labelleft=False,
                   labelright=False, labeltop=False)
    # 目盛り軸を消す
    ax.w_xaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
    ax.w_yaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
    ax.w_zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
    # 目盛を消す
    ax.xaxis._axinfo["tick"]["color"] = (1, 1, 1, 0)
    ax.yaxis._axinfo["tick"]["color"] = (1, 1, 1, 0)
    ax.zaxis._axinfo["tick"]["color"] = (1, 1, 1, 0)

    # 軸
    # 軸位置変更
    ax.xaxis._axinfo["juggled"] = (0, 0, 0)
    ax.yaxis._axinfo["juggled"] = (1, 1, 1)
    ax.zaxis._axinfo["juggled"] = (2, 2, 2)

    # データ
    # 直交座標
    arrow_head_scale = 20
    axis_line_width = 2
    arrow_style = "-|>"
    axis_x = Arrow3D([0, 1], [0, 0], [0, 0], mutation_scale=arrow_head_scale,
                     linewidth=axis_line_width, arrowstyle=arrow_style, color="red")
    axis_y = Arrow3D([0, 0], [0, 1], [0, 0], mutation_scale=arrow_head_scale,
                     linewidth=axis_line_width, arrowstyle=arrow_style, color="green")
    axis_z = Arrow3D([0, 0], [0, 0], [0, 1], mutation_scale=arrow_head_scale,
                     linewidth=axis_line_width, arrowstyle=arrow_style, color="blue")
    # テキスト
    label_size = 20
    label_offset = 0.05
    font_family = "Times New Roman"
    ax.text(1+label_offset, 0, 0, "x", size=label_size,
            verticalalignment="center", horizontalalignment="center", fontfamily=font_family)
    ax.text(0, 1+label_offset, 0, "y", size=label_size,
            verticalalignment="center", horizontalalignment="center", fontfamily=font_family)
    ax.text(0, 0, 1+label_offset, "z", size=label_size,
            verticalalignment="center", horizontalalignment="center", fontfamily=font_family)
    ax.text(0.15, 0.15, 0, "O", size=label_size,
            verticalalignment="center", horizontalalignment="center", fontfamily=font_family)

    # プロット
    ax.add_artist(axis_x)
    ax.add_artist(axis_y)
    ax.add_artist(axis_z)
    ax.plot([0], [0], [0], marker="o", color="black")  # 原点

    # 描画範囲
    ax.set_xlim3d(0, 1)
    ax.set_ylim3d(0, 1)
    ax.set_zlim3d(0, 1)

    # 視点
    ax.view_init(elev=30, azim=45)

    # 描画＆ファイル保存
    fig.savefig(os.path.splitext(os.path.basename(__file__))[0])
    plt.show()


if __name__ == '__main__':
    main()
