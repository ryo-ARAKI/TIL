# LaTeXのTipsなどの備忘録

## `\underbrace{}`の表示がおかしい

- mathabxとmathtoolsパッケージを同時に使うとおかしくなる．→一方のみ読み込めば解決．
- [mathabx + mathtools -> extremely odd underbrace behaviour… how to fix?](https://tex.stackexchange.com/questions/117628/mathabx-mathtools-extremely-odd-underbrace-behaviour-how-to-fix)

## `siunitx`を使った単位付き数値をmath環境で使う際の最適解

```latex
\SI{9.81}{\meter/\second^2}
```

と同じ出力は

```latex
\(9.81\, \si{\meter/\second^2}\)
```

で得られる

- [The “correct” or recommended way of using siunitx in math mode](https://tex.stackexchange.com/questions/451967/the-correct-or-recommended-way-of-using-siunitx-in-math-mode)

## footnote番号（アルファベット）や`\subfloat`の図番号がオーバーフローしてしまう

- footnote番号をページごとにリセットする

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
