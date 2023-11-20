# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib
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

    # 目盛り
    # グリッド用に値は設定しておく
    axis_length = 1.3
    ax.set_xticks(np.arange(0.1, axis_length, 0.1))
    ax.set_yticks(np.arange(0.1, axis_length, 0.1))
    ax.set_zticks(np.arange(0.1, axis_length, 0.1))
    # 目盛りラベルを消す
    ax.tick_params(labelbottom=False, labelleft=False,
                   labelright=False, labeltop=False)
    # 目盛り軸を消す
    ax.w_xaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
    ax.w_yaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
    ax.w_zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
    # 目盛りを消す
    ax.xaxis._axinfo["tick"]["color"] = (1, 1, 1, 0)
    ax.yaxis._axinfo["tick"]["color"] = (1, 1, 1, 0)
    ax.zaxis._axinfo["tick"]["color"] = (1, 1, 1, 0)

    # 軸
    # 軸位置変更
    ax.xaxis._axinfo["juggled"] = (0, 0, 0)
    ax.yaxis._axinfo["juggled"] = (1, 1, 1)
    ax.zaxis._axinfo["juggled"] = (2, 2, 2)

    # データ
    radius = 1.0
    theta = np.pi/4
    phi = np.pi/4
    # 点
    point_x = radius*np.sin(theta)*np.cos(phi)
    point_y = radius*np.sin(theta)*np.sin(phi)
    point_z = radius*np.cos(theta)
    # radius
    radius_x = [0, point_x]
    radius_y = [0, point_y]
    radius_z = [0, point_z]
    # theta
    theta_linspace = np.linspace(0, theta, 100)
    theta_r = 0.3
    theta_x = theta_r*np.sin(theta_linspace)*np.cos(phi)
    theta_y = theta_r*np.sin(theta_linspace)*np.sin(phi)
    theta_z = theta_r*np.cos(theta_linspace)
    # phi
    phi_linspace = np.linspace(0, phi, 100)
    phi_r = 0.3
    phi_x = phi_r*np.cos(phi_linspace)
    phi_y = phi_r*np.sin(phi_linspace)
    phi_z = [0]
    # 垂線
    # line_perpendicular_x = [point_x, point_x]
    # line_perpendicular_y = [point_y, point_y]
    # line_perpendicular_z = [point_z, 0]
    # 原点からphi方向
    line_phi_x = [0, np.cos(phi)]
    line_phi_y = [0, np.sin(phi)]
    line_phi_z = [0, 0]
    # theta cicle
    theta_circle_linspace = np.linspace(0, np.pi/2, 100)
    theta_circle_r = 1
    theta_circle_x = theta_circle_r*np.sin(theta_circle_linspace)*np.cos(phi)
    theta_circle_y = theta_circle_r*np.sin(theta_circle_linspace)*np.sin(phi)
    theta_circle_z = theta_circle_r*np.cos(theta_circle_linspace)
    # phi cicle
    phi_circle_linspace = np.linspace(0, np.pi/2, 100)
    phi_circle_r = 1
    phi_circle_x = phi_circle_r*np.cos(phi_circle_linspace)
    phi_circle_y = phi_circle_r*np.sin(phi_circle_linspace)
    phi_circle_z = [0]

    # テキスト
    plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams["mathtext.fontset"] = "stix"
    # boldsymbolで必要
    plt.rc('text', usetex=True)
    plt.rcParams['text.latex.preamble'] = [r"\usepackage{amsmath}"]
    label_size = 20
    label_offset = 0.05
    polar_label_offset = 1.6
    ax.text(axis_length+label_offset, 0, 0, "x", size=label_size,
            verticalalignment="center", horizontalalignment="center")
    ax.text(0, axis_length+label_offset, 0, "y", size=label_size,
            verticalalignment="center", horizontalalignment="center")
    ax.text(0, 0, axis_length+label_offset, "z", size=label_size,
            verticalalignment="center", horizontalalignment="center")
    ax.text(0, -0.07, 0, "O", size=label_size,
            verticalalignment="center", horizontalalignment="center")
    ax.text(point_x/2, point_y/2, point_z/2, "r", size=label_size,
            verticalalignment="bottom", horizontalalignment="right")
    ax.text(np.median(phi_x)*polar_label_offset, np.median(phi_y)*polar_label_offset, np.median(phi_z), r"$\phi$", size=label_size,
            verticalalignment="center", horizontalalignment="center")
    ax.text(np.median(theta_x)*polar_label_offset, np.median(theta_y)*polar_label_offset, np.median(theta_z)*polar_label_offset, r"$\theta$", size=label_size,
            verticalalignment="center", horizontalalignment="center")
    ax.text(point_x+label_offset, point_y+label_offset, point_z+label_offset, r"$\boldsymbol{\mathrm{p}}$ = (r, $\theta$, $\phi$)", size=label_size,
            verticalalignment="bottom", horizontalalignment="left")

    # プロット
    # 軸・原点
    arrow_head_scale = 20
    axis_line_width = 1
    arrow_style = "-|>"
    axis_x = Arrow3D([0, axis_length], [0, 0], [0, 0], mutation_scale=arrow_head_scale,
                     linewidth=axis_line_width, arrowstyle=arrow_style, color="black")
    axis_y = Arrow3D([0, 0], [0, axis_length], [0, 0], mutation_scale=arrow_head_scale,
                     linewidth=axis_line_width, arrowstyle=arrow_style, color="black")
    axis_z = Arrow3D([0, 0], [0, 0], [0, axis_length], mutation_scale=arrow_head_scale,
                     linewidth=axis_line_width, arrowstyle=arrow_style, color="black")
    ax.add_artist(axis_x)
    ax.add_artist(axis_y)
    ax.add_artist(axis_z)
    ax.plot([0], [0], [0], marker="o", color="black")
    # 点
    ax.plot([point_x], [point_y], [point_z], marker="o", color="black")
    # radius
    arrow_radius = Arrow3D(radius_x, radius_y, radius_z, mutation_scale=arrow_head_scale,
                           linewidth=2, arrowstyle=arrow_style, color="red")
    ax.add_artist(arrow_radius)
    # theta
    ax.plot(theta_x, theta_y, theta_z, linewidth=2, color="green")
    arrow_theta = Arrow3D([theta_x[-2], theta_x[-1]], [theta_y[-2], theta_y[-1]], [theta_z[-2], theta_z[-1]], mutation_scale=arrow_head_scale,
                          linewidth=2, arrowstyle=arrow_style, color="green")
    ax.add_artist(arrow_theta)
    # phi
    ax.plot(phi_x, phi_y, phi_z, linewidth=2, color="blue")
    arrow_phi = Arrow3D([phi_x[-2], phi_x[-1]], [phi_y[-2], phi_y[-1]], [phi_z[0], phi_z[0]], mutation_scale=arrow_head_scale,
                        linewidth=2, arrowstyle=arrow_style, color="blue")
    ax.add_artist(arrow_phi)
    # 垂線
    # ax.plot(line_perpendicular_x, line_perpendicular_y,
    #         line_perpendicular_z, ":", linewidth=1, color="black")
    # 原点からphi方向
    ax.plot(line_phi_x, line_phi_y,
            line_phi_z, ":", linewidth=1, color="black")
    # theta cicle
    ax.plot(theta_circle_x, theta_circle_y,
            theta_circle_z, ":", linewidth=1, color="black")
    # phi cicle
    ax.plot(phi_circle_x, phi_circle_y,
            phi_circle_z, ":", linewidth=1, color="black")

    # 描画範囲
    ax.set_xlim3d(0, axis_length)
    ax.set_ylim3d(0, axis_length)
    ax.set_zlim3d(0, axis_length)

    # 視点
    ax.view_init(elev=30, azim=20)

    # 描画＆ファイル保存
    fig.savefig(os.path.splitext(os.path.basename(__file__))[0])
    plt.show()


if __name__ == '__main__':
    main()
