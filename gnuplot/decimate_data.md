# データを間引いて描画する

```gnuplot
plot "data.dat" every i:I:s:S:e:E u 1:2
```

- `i`：データ行の増分
- `I`：データブロックの増分
- `s`：開始行
- `S`：開始ブロック
- `e`：終了行
- `E`：終了ブロック

- 参考： [GNUPLOTに関するメモ](http://www.kusastro.kyoto-u.ac.jp/~moritani/etc/memo/gnuplot_memo.html)
