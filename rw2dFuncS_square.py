# Function to calculate properties of 2d Random Walk (square lattice model) (single run)

import numpy as np
import random as rd
from math import *
#import matplotlib.pyplot as plt

def rw2dFuncS(N):

    num = 0
    x, y = 0, 0
    x_list = [0]
    y_list = [0]
#    coordinate_list = [[0,0]]
#    imgs = []

    direction_list = ([1,0],[-1,0],[0,1],[0,-1])

    for n in range(N):
        step = rd.choice(direction_list)
        x = x + step[0]
        y = y + step[1]
        x_list.append(x)
        y_list.append(y)
#        coordinate = [x, y]
#        coordinate_list.append(coordinate)
        num = num + 1
#        img1 = plt.plot(x_list, y_list, color="cyan")
#        img2 = plt.plot(x_list[-1], y_list[-1], marker="x", color="black")
#        img = img1 + img2
#        imgs.append(img)    
#    print("final num = "+str(num)) # to check the number of steps
#    img1 = plt.plot(x_list, y_list, color="cyan")
#    img2 = plt.plot(x_list[-1], y_list[-1], marker="o", color="red")
#    img = img1 + img2
#    for i in range(10):
#        imgs.append(img)

#    print(x_list[-1], y_list[-1])
    coordinateS_list = [x_list, y_list]
    r2 = x_list[-1]*x_list[-1] + y_list[-1]*y_list[-1]
    r = np.sqrt(r2)
    resultS_list = [r2, r]


    return coordinateS_list, resultS_list