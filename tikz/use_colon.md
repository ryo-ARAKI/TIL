# `tikzpicture` 環境中でコロン記号を使う

TikZは `commath` による「アクティブなコロン」を上書きしてしまう．
プリアンブルに以下のように書くとコロン記号が使えるようになる

```latex
\usepackage{commath}
\makeatletter
\protected\def\tikz@nonactivecolon{\ifmmode\mathrel{\mathop\ordinarycolon}\else:\fi}
\makeatother
```

- 参考：[Why does pdfTeX hang on this file?](https://tex.stackexchange.com/questions/89467/why-does-pdftex-hang-on-this-file)
  - ただし，上記の方法もあまり良くないらしい
  - `mathtoolbox` パッケージを使う方法もあるが，上手くいかなかった
