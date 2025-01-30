# 2d Random Walk

import numpy as np
from math import *
import rw2dFuncS_square as rws
import rw2dFunc_fractal as rwf
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time

# Calculation of 2d Random Walk

try:
    N = int(input('Degree of polymerization (default=1000): '))
except ValueError:
    N = 1000

try:
    M = int(input('Number of repetition (default=100): '))
except ValueError:
    M = 100

try:
    radi = int(input('Radius for coarse-graining (default=3): '))
except ValueError:
    radi = 3

start_time = time.process_time()

coordinateS_list, resultS_list = rws.rw2dFuncS(N)

x_list_orig = coordinateS_list[0]
y_list_orig = coordinateS_list[1]
x_list = x_list_orig
y_list = y_list_orig

x_max = np.max([ np.abs(x) for x in x_list_orig ])
y_max = np.max([ np.abs(y) for y in y_list_orig ])
c_max = np.max([x_max, y_max])

# r2 = resultS_list[0]
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
print("NumRep = ", numRep)
oP_list = [sum(oP_list[:numRep-i]) for i in range(numRep)]
oP_list = [oP_list[numRep-i-1] for i in range(numRep)]

end_time = time.process_time()
elapsed_time = end_time - start_time

print('total time = {0:.5f} s'.format(elapsed_time))

# Plot of 2d Random Walk

x_range = c_max * 1.5
y_range = c_max * 1.5

ax1_title = "2D Random Walk (square) ($N$ = {0:.0f})".format(N)
ax2_title = "Distance from Origin, $R$($N$)"


resultText_r = "$R$($N$={0:.0f}) = {1:.1f}".format(N,r)
resultText_n = "$N_{{circ}}$ = {0:.0f}".format(numRep)

fig = plt.figure(figsize=(8.0, 4.0))

ax1 = fig.add_subplot(121,title=ax1_title, xlabel='$X$', ylabel='$Y$',
                      xlim=[-x_range, x_range], ylim=[-y_range , y_range])
ax1.grid(axis='both', color="gray", lw=0.5)
ax1.plot(x_list_orig, y_list_orig)
ax1.plot(x_list_orig[0], y_list_orig[0], marker=".", color="red")
ax1.plot(x_list_orig[N], y_list_orig[N], marker=".", color="red")
circ = patches.Circle(xy=(0, 0), radius=radi, ec='r', fill=False)
ax1.add_patch(circ)
for i in range(numRep-1):
    x_oP = x_list_orig[oP_list[i+1]]
    y_oP = y_list_orig[oP_list[i+1]]
    ax1.plot(x_oP, y_oP, marker=".", color="blue")
    circ = patches.Circle(xy=(x_oP, y_oP), radius=radi, ec='r', fill=False)
    ax1.add_patch(circ)


ax2 = fig.add_subplot(122, title=ax2_title, xlabel='$N$', ylabel='$R$($N$)',)
ax2.grid(axis='both', color="gray", lw=0.5)
ax2.plot(dist_list_orig)

fig.text(0.15, 0.80, resultText_r)
fig.text(0.15, 0.70, resultText_n)

savefile = "./png/rw2d_square_N{0:.0f}_R{1:.0f}_fractal.png".format(N,radi)

fig.savefig(savefile, dpi=300, bbox_inches='tight')

#plt.tight_layout()
plt.show()
