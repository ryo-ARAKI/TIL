# footnote番号（アルファベット）や `\subfloat` の図番号のオーバーフローを抑制する

- footnote番号をページごとにリセットする

```latex
\usepackage[perpage]{footmisc}
\renewcommand{\thefootnote}{\fnsymbol{footnote}}
```

- `subfigure` 番号を適宜リセットする

```latex
\setcounter{subfigure}{0}
```
