#coding=utf-8
from matplotlib import pyplot as plt
import matplotlib
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def s3dDemo1():

    # 下面这段话，是利用numpy包读取csv里面的数据，然后分别取出X\Y\Z三维值
    eq2013 = np.loadtxt('train.csv', dtype=np.str, delimiter=",")
    data = eq2013[1:, 0:].astype(np.float)
    X = data[:, 0]
    Y = data[:, 1]
    Z = data[:, 3] * -1
    C = []
    # 下面这循环是根据Z值（地震深度）设置颜色
    for z in Z:
        if z >= -60:
            C.append("r")
        elif z < -300:
            C.append("k")
        else:
            C.append("y")

    ax = plt.figure().add_subplot(111, projection='3d')
    # 基于ax变量绘制三维图
    # xs表示x方向的变量
    # ys表示y方向的变量
    # zs表示z方向的变量，这三个方向上的变量都可以用list的形式表示
    # m表示点的形式，o是圆形的点，^是三角形（marker)
    # c表示颜色（color for short）
    ax.scatter(X, Y, Z, c='r', marker='^')  # 点为红色三角形

    # 设置坐标轴
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    # 显示图像
    plt.show()

s3dDemo1()
