# Scatterプロットのscatter部分のみをラスタライズして高速化する

```Python
ax.scatter(
    x, y,
    rasterized=True
)
```

- 参考：
  - [savefig SVG and PDF output for scatter plots is excessively complex, crashses Inkscape](https://github.com/matplotlib/matplotlib/issues/5967/)
  - [Rasterization for vector graphics](https://matplotlib.org/devdocs/gallery/misc/rasterization_demo.html)
