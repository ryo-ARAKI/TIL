# Gnuplotの備忘録

## データを間引いて描画する

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

## 描画範囲を指定する

例えば

```dat
# 時刻 データ
0.0 1.0
0.1 2.0
0.2 3.0
...
```

というデータに対し，時刻>100の範囲だけプロットしたいときは

```gnuplot
plot 1:($1>100?$2:1/0)
```

でできる．

## 凡例を前面に出力する

```gnuplot
set key opaque
```

## `.gp` スクリプトで描画したグラフを表示し続ける

スクリプト末尾に以下のように書けば良い

```gnuplot
pause mouse close
```

## y=0を描画しない

```gnuplot
plot "mydataset.dat" u 1:($2 == 0 ? NaN : $2)
```

- 参考：[Ignore points with y=0](https://stackoverflow.com/a/11867671)