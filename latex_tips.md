# LaTeX の Tips や備忘録

## `\underbrace{}`の表示がおかしい

- mathabx と mathtools パッケージを同時に使うとおかしくなる．→ 一方のみ読み込めば解決．
- [mathabx + mathtools -> extremely odd underbrace behaviour… how to fix?](https://tex.stackexchange.com/questions/117628/mathabx-mathtools-extremely-odd-underbrace-behaviour-how-to-fix)

## `siunitx`を使った単位付き数値を math 環境で使う際の最適解

```latex
\SI{9.81}{\meter/\second^2}
```

と同じ出力は

```latex
\(9.81\, \si{\meter/\second^2}\)
```

で得られる

- [The “correct” or recommended way of using siunitx in math mode](https://tex.stackexchange.com/questions/451967/the-correct-or-recommended-way-of-using-siunitx-in-math-mode)

## footnote 番号（アルファベット）や`\subfloat`の図番号がオーバーフローしてしまう

- footnote 番号をページごとにリセットする

```latex
\usepackage[perpage]{footmisc}
\renewcommand{\thefootnote}{\fnsymbol{footnote}}
```

- `subfigure`番号を適宜リセットする

```latex
\setcounter{subfigure}{0}
```

## `itemize`環境内でテキストを揃えたい

- `makebox`を使う

```latex
\begin{itemize}
  \item{\makebox[2cm][l]{$x$} is a continuous random variable.}
  \item{\makebox[2cm][l]{$f_X(x)$} is the PDF of $x$.}
  \item{\makebox[2cm][l]{$g(x)$} is a function of $x$.}
\end{itemize}
```

- [Custom alignment of text in itemized environment](https://tex.stackexchange.com/questions/147679/custom-alignment-of-text-in-itemized-environment)

## ダミー文章や図を挿入したい

### 英語：[lipsum](https://www.ctan.org/pkg/lipsum)パッケージ

```latex
# preample
\usepackage{lipsum}

# document
\lipsum[1-3]
```

### 日本語：[bxjalipsum](https://github.com/zr-tex8r/BXjalipsum)パッケージ

```latex
# preample
\usepackage{bxjalipsum}

# document
\jalipsum{iroha}  # いろは
\jalipsum{jugemu}  # 寿限無
\jalipsum[1-33]{wagahai}  # 吾輩は猫である
\jalipsum[1-4]{preamble}  # 憲法前文
\jalipsum[1-4]{hatsukoi}  # 初恋
```

### 図：[mwe](https://www.ctan.org/pkg/mwe)パッケージ

```latex
\includegraphics[width=0.6\textwidth]{example-image}
\includegraphics[width=0.6\textwidth]{example-image-16x9}
```

## `\underline{}` 中で改行できない

- 代替パッケージを使う：[下線に関するマクロ比較](http://www9.oninet.ne.jp/ohishi/tex/library/underline.pdf)

  > - `udline.sty` で定義されている `\ul` コマンド
  > - `jumoline.sty` (横組み用) で定義されている `\Underline` コマンド
  > - `jundline.sty` (横組み用) で定義されている `\jundline` コマンド
  > - `ulem.sty` で定義されている `\uline` コマンド (欧文専用) [下線拡張パッケージ udline.sty](http://minamo.my.coocan.jp/tex/udline.html)

### `ulem.sty` の導入と調節

- `sudo apt install texlive-generic-recommended` あるいは
- `sudo apt install texlive-plain-generic` （Ubuntu 20）
  で導入できる．
  - 参考：[Why am I getting missing packages in Tex](https://askubuntu.com/a/936359)
  - また， `\uline{text}` だと下線が細すぎるが `{\def\ULthickness{1pt}\uline{text}}` のようにすれば太さを変更できる．
