# TikZ の備忘録

## 参考にしたサイト

- [九州大学附属図書館：Tikz を使ってみよう！](https://guides.lib.kyushu-u.ac.jp/c.php?g=774891&p=5559083)
- [Beamer のための TikZ](https://www.opt.mist.i.u-tokyo.ac.jp/~tasuku/tikz.html)
- [Visual Tikz](http://ftp.jaist.ac.jp/pub/CTAN/info/visualtikz/VisualTikZ.pdf)

## 基本

プリアンプルで

```latex
\usepackage{tikz}
\usetikzlibrary{positioning}
```

のようにして，

```latex
\begin{tikzpicture}
  hoge
\end{tikzpicture}
```

環境中にコマンドを記述する

## 図形など

```latex
# 長方形
\draw (0,0) rectangle (2,3);
# 円弧で繋がれた長方形
\draw[thick, rounded corners=10pt](0,0)--(0,3)--(2,3)--(2,0)-- cycle;
# 円
\draw(0,0) circle (1cm);
# 楕円
\draw(0,0) circle (1.2cm and 0.5cm);
# 格子
\draw[step=0.5, very thin, gray] (-1.4, -1.4) grid (1.4, 1.4);
```

### 文章の追加

```latex
\draw[->, very thick] (0,0) node[below]{ここから} -- (2,2) node[above]{ここまで};
```

文章を左揃えで改行したいときは

```latex
\node[draw, align=left] {一行目と\\二行目};
```

### 繰り返し処理

```latex
# (x,y)軸とticks
\draw[->] (0, -3.5) -- (0, 3.5);
\draw[->] (-3.5, 0) -- (3.5, 0);
\draw (-0.3, -0.1) node[below]{0};
\foreach \x in {-3, -2, -1, 1, 2, 3}
  \draw (\x, -0.1) node[below]{\x} -- (\x, 0.1);
\foreach \y in {-3, -2, -1, 1, 2, 3}
  \draw (-0.1, \y) node[left]{\y} -- (0.1, \y);
```

## 数式の装飾

`mystyle_beamer.sty` に以下を定義している

```latex
\newcommand{\highlight}[2][yellow]{\tikz[baseline=(x.base)]{\node[rectangle,rounded corners,fill=#1!10](x){#2};}}
\newcommand{\highlightcap}[3][yellow]{\tikz[baseline=(x.base)]{\node[rectangle,rounded corners,fill=#1!10](x){#2} node[below of=x, color=#1]{#3};}}
```

これを用いてマーカーを引いたり説明をつけたりできる

```latex
\highlightcap[red]{\(\displaystyle \qty(\vb*{u} \cdot) \grad{\vb*{u}} \)}{非線形項}
```
