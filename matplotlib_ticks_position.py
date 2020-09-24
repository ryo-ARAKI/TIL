########################################################################
#
#  Matplotlibで軸のticks位置を調整するサンプルプログラム
#  https://www.pynote.info/entry/matplotlib-xticks-yticks-grid
#  をベースに
#  https://stackoverflow.com/questions/28615887/how-to-move-a-ticks-label-in-matplotlib
#  を参考にticks位置を修正
#
########################################################################


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.transforms

# データ生成
x = np.linspace(0, np.pi * 4, 100)
y = np.sin(x)

# プロット
fig, ax = plt.subplots(facecolor="w")
ax.plot(x, y)

# ticksの数の指定
ax.set_xticks(np.linspace(0, np.pi * 4, 5))
ax.set_xticks(np.linspace(0, np.pi * 4, 17), minor=True)
ax.set_yticks(np.linspace(-1, 1, 3))
ax.set_yticks(np.linspace(-1, 1, 5), minor=True)

# ========================================
# y軸のticks labelの位置の指定
dx = -10/72.  # matplotlibは72ppi（point per inch）を使っているのでそれ基準で移動ポイント数を指定する
dy = 0/72.
offset = matplotlib.transforms.ScaledTranslation(dx, dy, fig.dpi_scale_trans)

# apply offset transform to all y ticklabels.
for label in ax.yaxis.get_majorticklabels():
    label.set_transform(label.get_transform() + offset)
# ========================================


# グラフ保存
plt.tight_layout()  # フォントサイズ変更によるグラフのレイアウトズレを修正
plt.savefig(
    'sin.pdf',
    dpi=300,
    bbox_inches='tight', pad_inches=0.1)
print("DONE: output_scalar plot")
