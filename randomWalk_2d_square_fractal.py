# 2d Random Walk

import numpy as np
from math import *
import rw2dFunc_fractal_M as rwfm
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

# try:
#    radi = int(input('Radius for coarse-graining (default=3): '))
# except ValueError:
#    radi = 3

radi_list = np.logspace(np.log10(3), np.log10(np.sqrt(N)), num=10)
print(radi_list)
radi_list = [radi_list[9-i] for i in range(10)] # 大きいradiから始めて最後は小さいradiで画像を残したので順序を逆にした

numRep_mean_list = []
numRep_std_list = []

for radi in radi_list:
    start_time = time.process_time()

    numRep_list = []

    for i in range(M):
        coordinateM_list, resultM_list = rwfm.rw2d_fractal(N, radi)
        x_list_orig    = coordinateM_list[0]
        y_list_orig    = coordinateM_list[1]
        dist_list_orig = coordinateM_list[2]
        oP_list        = coordinateM_list[3]
        r      = resultM_list[0]
        c_max  = resultM_list[1]
        numRep = resultM_list[2]
        numRep_list.append(numRep)

    numRep_mean_list.append(np.mean(numRep_list))

    end_time = time.process_time()
    elapsed_time = end_time - start_time
    print('total time = {0:.5f} s'.format(elapsed_time))

log_radi_list = [ log10(x) for x in radi_list ]
log_numRep_mean_list = [ log10(x) for x in numRep_mean_list ]

# Least-squares fitting

fit_result, fit_error = np.polyfit(log_radi_list, log_numRep_mean_list, 1, cov=True)
exponent = fit_result[0]
intercept = fit_result[1]
exponent_error = np.sqrt(fit_error[0,0])
fit_func = np.poly1d(fit_result)(log_radi_list)

# Plot of 2d Random Walk

x_range = c_max * 1.5
y_range = c_max * 1.5

ax1_title = "2D Random Walk (square) ($N$ = {0:.0f})".format(N)
ax2_title = "Distance from origin"
ax3_title = "2D Random Walk (square) ($N$ = {0:.0f})".format(N)
ax4_title = "Fractal Analysis ($M$ = {0:.0f})".format(M)

resultText_r = "$R$($N$={0:.0f}) = {1:.1f}".format(N,r)
resultText_n = "$N_{{circ}}$ = {0:.0f}".format(numRep)
resultText_radi = "$r$ = {0:.1f}".format(radi)
resultText_f = "$N_{{circ}}$ ~ $r^{{{{{0:.3f}}}±{{{1:.3f}}}}}$".format(exponent,exponent_error)
resultText_t = "$T_{{comp}}$ = {0:.2f} s".format(elapsed_time)

fig = plt.figure(figsize=(10.0, 9.0))

ax1 = fig.add_subplot(221,title=ax1_title, xlabel='$X$', ylabel='$Y$',
                      xlim=[-x_range, x_range], ylim=[-y_range , y_range])
ax1.grid(axis='both', color="gray", lw=0.5)
ax1.plot(x_list_orig, y_list_orig)
ax1.plot(x_list_orig[0], y_list_orig[0], marker=".", color="red")
ax1.plot(x_list_orig[N], y_list_orig[N], marker=".", color="red")

ax2 = fig.add_subplot(222, title=ax2_title, xlabel='$N$', ylabel='$R$($N$)',)
ax2.grid(axis='both', color="gray", lw=0.5)
ax2.plot(dist_list_orig)

ax3 = fig.add_subplot(223,title=ax3_title, xlabel='$X$', ylabel='$Y$',
                      xlim=[-x_range, x_range], ylim=[-y_range , y_range])
ax3.grid(axis='both', color="gray", lw=0.5)
ax3.plot(x_list_orig, y_list_orig)
ax3.plot(x_list_orig[0], y_list_orig[0], marker=".", color="red")
ax3.plot(x_list_orig[N], y_list_orig[N], marker=".", color="red")
circ = patches.Circle(xy=(0, 0), radius=radi, ec='r', fill=False)
ax3.add_patch(circ)
for i in range(numRep-1):
    x_oP = x_list_orig[oP_list[i+1]]
    y_oP = y_list_orig[oP_list[i+1]]
    ax3.plot(x_oP, y_oP, marker=".", color="blue")
    circ = patches.Circle(xy=(x_oP, y_oP), radius=radi, ec='r', fill=False)
    ax3.add_patch(circ)

ax4 = fig.add_subplot(224, title=ax4_title, xlabel='Log($r$)', ylabel='Log($N_{{circ}}$)')
ax4.grid(axis='both', color="gray", lw=0.5)
ax4.scatter(log_radi_list, log_numRep_mean_list)
ax4.plot(log_radi_list, fit_func, color="black")

fig.text(0.15, 0.85, resultText_r)
fig.text(0.15, 0.42, resultText_n)
fig.text(0.15, 0.37, resultText_radi)
fig.text(0.60, 0.20, resultText_f)
fig.text(0.60, 0.15, resultText_t)

savefile = "./png/rw2d_square_N{0:.0f}_M{1:.0f}_fractal.png".format(N,M)

fig.savefig(savefile, dpi=300, bbox_inches='tight')

#plt.tight_layout()
plt.show()
