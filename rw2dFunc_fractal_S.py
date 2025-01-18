# Function to calculate properties of 2d Random Walk (square lattice model) (single run)
# フラクタル解析のために必要な関数を定義している

import numpy as np
import random as rd
from math import *

def rw2d_dist(x_list, y_list, num):
    dist_list = []

    for i in range(num+1):
        x = x_list[i]
        y = y_list[i]
        dist = np.sqrt(x*x + y*y)
        dist_list.append(dist)
        i = i + 1

    dist_list = list(map(float, dist_list))  # np.sqrtでnp.float64になったのをただのリストに戻した

    return dist_list

def rw2d_slice(dist_list, x_list, y_list, radi):
# この辺はちゃんとスライスできているかの確認（最終的には不要）
#    for i in range(num+1):
#        print(dist_list[i])
# ここまで
    j = 0    
    while dist_list[j] < radi:
        j = j + 1
    else:
# この辺はちゃんとスライスできているかの確認（最終的には不要）
#        print(j-1)
#        print(dist_list[j-1])
#        print(dist_list[j])
#        updated_dist_list = dist_list[j-1:]
#        print(updated_dist_list)
# ここまで
        oPoint = j-1  
        updated_x_list = x_list[oPoint:]
        updated_y_list = y_list[oPoint:]
        updated_num = len(updated_x_list)
        updated_x_list = [x - updated_x_list[0] for x in updated_x_list]
        updated_y_list = [y - updated_y_list[0] for y in updated_y_list]

    return updated_x_list, updated_y_list, oPoint, updated_num