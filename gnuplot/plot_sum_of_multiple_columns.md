# 複数の列データの和を描画する

`filename` にあるデータの1列目をx軸，2-10列目の和をy軸としてプロットする

```gnuplot
plot "filename" 1:(sum [col=2:10] column(col))
```

- 参考：[1.14.3 Summation](http://www.chiark.greenend.org.uk/doc/gnuplot-doc/htmldocs/Summation.html)
