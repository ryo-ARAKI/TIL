# 複数の列データの和を描画する

`filename` にあるデータの 1 列目を x 軸，2-10 列目の和を y 軸としてプロットする

```gnuplot
plot "filename" 1:(sum [col=2:10] column(col))
```

- 参考：[1.14.3 Summation](http://www.chiark.greenend.org.uk/doc/gnuplot-doc/htmldocs/Summation.html)
