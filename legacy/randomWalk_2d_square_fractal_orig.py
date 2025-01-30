# 2d Random Walk

import numpy as np
from math import *
# from scipy.stats import norm
import rw2dFuncS_square_fractal as rws
import rw2dFuncM_square as rwm
import rw2dFunc_Fractal as rwf
import matplotlib.pyplot as plt
import time

# Calculation of 2d Random Walk

try:
    N = int(input('Degree of polymerization (default=15): '))
except ValueError:
    N = 15

#try:
#    M = int(input('Number of repetition (default=1000): '))
#except ValueError:
#    M = 1000

start_time = time.process_time()

# logN = log10(N)
# logM = log10(M)

coordinateS_list, resultS_list = rws.rw2dFuncS(N)
# coordinateM_list, resultM_list = rwm.rw2dFuncM(N, M)

x_list = coordinateS_list[0]
y_list = coordinateS_list[1]

print(len(x_list))

r2 = resultS_list[0]
r = resultS_list[1]

dist_list = rwf.rw2d_dist(x_list, y_list, N)
l = len(dist_list)
print(len(dist_list))

radi = 2

updated_x_list, updated_y_list, updated_num = rwf.rw2d_slice(dist_list, x_list, y_list, radi, N)

print(updated_num)

dist_list2 = rwf.rw2d_dist(updated_x_list, updated_y_list, updated_num-1)
l = len(dist_list2)
print(len(dist_list2))

# xt_list = coordinateM_list[0]
# yt_list = coordinateM_list[1]
# r_list = coordinateM_list[3]

# x_max = np.max(xt_list)
# y_max = np.max(yt_list)
# r_max = np.max(r_list)

# r2_mean = resultM_list[0]
# r2_std = resultM_list[1]
# r_mean = resultM_list[2]
# r_std = resultM_list[3]
# x_mean = resultM_list[4]
# x_std = resultM_list[5]
# y_mean = resultM_list[6]
# y_std = resultM_list[7]

# R = np.sqrt(r2_mean)

# Least-squares fitting

# GaussX_mean,GaussX_std = norm.fit(xt_list)
# GaussY_mean,GaussY_std = norm.fit(yt_list)

# def fitFunc(x, a, b):
#    return  b * x * np.exp(-x*x/a)

end_time = time.process_time()
elapsed_time = end_time - start_time

print('total time = {0:.5f} s'.format(elapsed_time))

# Plot of 2d Random Walk

# x_range = x_max / sqrt(2)
# y_range = y_max / sqrt(2)

x_range = 20
y_range = 20

#ax1_title = "2D Random Walk (square) ($N$ = $10^{0:.0f}$, $M$ = $10^{1:.0f}$)".format(logN, logM)
ax1_title = "2D Random Walk (square) ($N$ = {0:.0f})".format(N)
ax2_title = "Distribution of $R$ = <$r^2>^{{1/2}}$"


resultText_r = "$r$ = {0:.1f}".format(r)
# resultText_rmean = "<$r$> = {1:.1f}".format(logM, r_mean)
# resultText_R = "$R$ = {1:.1f}".format(M, R)

fig = plt.figure(figsize=(8.0, 8.0))

ax1 = fig.add_subplot(221,title=ax1_title, xlabel='$X$', ylabel='$Y$',
                      xlim=[-x_range, x_range], ylim=[-y_range , y_range])
ax1.grid(axis='both', color="gray", lw=0.5)
ax1.plot(x_list, y_list)
ax1.plot(x_list[0], y_list[0], marker=".", color="red")
ax1.plot(x_list[N], y_list[N], marker=".", color="red")

ax2 = fig.add_subplot(222)
ax2.grid(axis='both', color="gray", lw=0.5)
ax2.plot(dist_list)

ax2 = fig.add_subplot(223)
ax2.grid(axis='both', color="gray", lw=0.5)
ax2.plot(dist_list2)




# np.savetxt("./data/hist_YX.txt", hist_YX)


fig.text(0.15, 0.60, resultText_r)
# fig.text(0.15, 0.58, resultText_rmean)
# fig.text(0.15, 0.56, resultText_R)


savefile = "./png/randomWalk_2d_square_N{0:.0f}.png".format(N)

fig.savefig(savefile, dpi=300, bbox_inches='tight')

#plt.tight_layout()
plt.show()
