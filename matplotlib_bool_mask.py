########################################################################
#  Matplotlibのplotで，boolean arrayを用いてグラフの一部だけを強調するプログラム
#  Simple plot https://matplotlib.org/gallery/lines_bars_and_markers/simple_plot.html#sphx-glr-gallery-lines-bars-and-markers-simple-plot-py
#  Boolean arrayを使って配列を分割する https://stackoverflow.com/a/36518315
########################################################################

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


#==================================================
# t∈[0, π], sin(2πt) のグラフをプロット
#==================================================
time = np.arange(0.0, np.pi, 0.01)
sine = np.sin(2 * np.pi * time)

fig, ax = plt.subplots()
ax.plot(
    time, sine,
    linewidth=2,
    color='black'
)

ax.set(
    xlabel='time (s)', ylabel='voltage (mV)',
    title='About as simple as it gets, folks'
)


#==================================================
# このグラフのうちt∈[0, π/4], [3π/4, π]だけ強調する
#==================================================

# boolean arrayを作成
bool_mask = np.full((len(time)), False, dtype=bool)
for itr in range(len(time)):
    if time[itr] <= np.pi/4 or time[itr] >= np.pi * 3/4:
        bool_mask[itr] = True

# boolean arrayで抽出した部分配列を作成
# https://stackoverflow.com/a/36518315
# 1. True/Falseが切り替わるインデックスを取得
indices = np.nonzero(bool_mask[1:] != bool_mask[:-1])[0] + 1

# 2. 配列を分割
time_split = np.split(time, indices)
sine_split = np.split(sine, indices)

# 3. 分割された配列を二つごとに選択
# ただしboolean arrayの先頭によって選択が変化することに注意
time_split = time_split[0::2] if bool_mask[0] else time_split[1::2]
sine_split = sine_split[0::2] if bool_mask[0] else sine_split[1::2]

# 4. 分割された配列を強調してプロット
for itr_split in range(np.shape(time_split)[0]):
    ax.plot(
        time_split[itr_split], sine_split[itr_split],
        linewidth=6,
        color='red',
        alpha=0.6
    )

plt.show()
