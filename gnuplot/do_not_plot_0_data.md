# y=0 を描画しない

```gnuplot
plot "mydataset.dat" u 1:($2 == 0 ? NaN : $2)
```

- 参考：[Ignore points with y=0](https://stackoverflow.com/a/11867671)
