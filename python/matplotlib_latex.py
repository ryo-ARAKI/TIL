########################################################################
#
#  MatplotlibでLaTeX書式を使うサンプルプログラム
#
########################################################################

# パッケージの導入
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rc

# グラフの設定
sns.set(
    context='talk',  # スライドに合ったフォントサイズ・線幅
    style='white',  # 背景白，グリッドなし
    palette='plasma',  # あらきお気に入りのカラースキーム
    font='sans-serif',  # フォント指定
    font_scale=1,  # フォントスケール指定（これを変えるとcontextで決まるプリセットを更にいじれる）
    rc={'text.usetex': True}  # LaTeX書式を使えるように
)
plt.rc('text.latex', preamble=r'\usepackage{physics}')

# データ作成
length = 200
max_n = 5
x = np.linspace(start=0.0, stop=2.0*np.pi, num=length)
y = np.empty((length, max_n))
for itr_n in range(max_n):
    y[:, itr_n] = np.sin(itr_n * np.pi * x)

# グラフ設定
filename = "plot_sin"
plt.close()
fig, ax = plt.subplots(figsize=(9, 6))
ax.set_xlim(
    [x[0], x[-1]]
)
ax.set_xlabel(r"$t$")
ax.set_ylabel(r"$\sin(n\pi x)$")
colors = plt.cm.plasma(np.linspace(0, 0.9, max_n))
legend = [
    r"$\sin(0)$",
    r"$\sin(\pi x)$",
    r"$\sin(2\pi x)$",
    r"$\sin(3\pi x)$",
    r"$\sin(4\pi x)$"
]

# プロット
for itr_data in range(np.shape(y)[1]):
    plt.plot(
        x,
        y[:, itr_data],
        linewidth=2,
        color=colors[itr_data],
        label=legend[itr_data]
    )

ax.legend(  # グラフに凡例を表示する
    loc='upper right',
    ncol=2  # 凡例の列数=データの種類の数
)

# グラフ保存
plt.tight_layout()  # フォントサイズ変更によるグラフのレイアウトズレを修正
plt.savefig(
    filename + '.pdf',
    dpi=300,
    bbox_inches='tight', pad_inches=0.1)
print("DONE: output_scalar plot")
