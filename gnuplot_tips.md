# Gnuplotの備忘録

## `every` command

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

## 描画範囲の指定

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

## 反例を前面に出力したい

```gnuplot
set key opaque
```

## `.gp` スクリプトで描画したグラフを表示し続けたい

スクリプト末尾に以下のように書けば良い

```gnuplot
pause mouse close
```
