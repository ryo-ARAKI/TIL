# Matplotlib の Tips や備忘録

## Scatterプロットをベクター形式で保存するとレンダリングに異常な時間がかかる

- プロット部分のみをラスタライズすると良い

```Python
ax.scatter(
    x, y,
    rasterized=True
)
```

- 参考：
  - [savefig SVG and PDF output for scatter plots is excessively complex, crashses Inkscape](https://github.com/matplotlib/matplotlib/issues/5967/)
  - [Rasterization for vector graphics](https://matplotlib.org/devdocs/gallery/misc/rasterization_demo.html)
