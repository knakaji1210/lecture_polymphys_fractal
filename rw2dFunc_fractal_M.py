# Function to calculate properties of 2d Random Walk (square lattice model) (multiple run)
# フラクタル解析のために必要な関数を定義している

import numpy as np
from math import *
import rw2dFuncS_square as rws
import rw2dFunc_fractal_S as rwf
import time

def rw2d_fractal(N, radi):
    coordinateS_list, resultS_list = rws.rw2dFuncS(N)

    x_list_orig = coordinateS_list[0]
    y_list_orig = coordinateS_list[1]
    x_list = x_list_orig
    y_list = y_list_orig

    x_max = np.max([ np.abs(x) for x in x_list_orig ])
    y_max = np.max([ np.abs(y) for y in y_list_orig ])
    c_max = np.max([x_max, y_max])

    r = resultS_list[1]

    # フラクタル解析のために追加した部分
    # ここはまず原点からの距離を求めている
    num = N
    dist_list_orig = rwf.rw2d_dist(x_list, y_list, num)
    dist_list = dist_list_orig
    # l = len(dist_list)
    # print(l)

    # ここで指定した半径内にある点の集合を繰り返しスライスしていく
    numRep = 1
    oP_list = [0]

    while np.max(dist_list) > radi:
        numRep = numRep + 1
        x_list, y_list, oP, num = rwf.rw2d_slice(dist_list, x_list, y_list, radi)
        dist_list = rwf.rw2d_dist(x_list, y_list, num-1)
    #    l = len(dist_list)
    #    print(len(dist_list))
        oP_list.append(oP)

    # ここで各スライスの原点を決めている
    # print("NumRep = ", numRep)
    oP_list = [sum(oP_list[:numRep-i]) for i in range(numRep)]
    oP_list = [oP_list[numRep-i-1] for i in range(numRep)]

    coordinateM_list = [x_list_orig, y_list_orig, dist_list_orig, oP_list]
    resultM_list = [r, c_max, numRep]

    return coordinateM_list, resultM_list

