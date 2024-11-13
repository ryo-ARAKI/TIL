# 目次の表示を制御する

- `\tableofcontents` に次のようなオプションを指定する

```latex
\tableofcontents[
  sectionstyle=show/shaded,
  subsectionstyle=show/show/shaded,
  subsubsectionstyle=show/show/show/shaded
]
```

- keyは `show, shaded, hide` の3種類
- `sectionstyle`
  1. 現在のsection
  2. それ以外のsection
- `subsectionstyle`
  1. 現在のsubsection
  2. 現在のsection中の他のsubsection
  3. 他のsection中のsubsection
- `subsubsectionstyle`

  1. 現在のsubsubsection
  2. 現在のsubsection中の他のsubsubsection
  3. 現在のsectionの他のsubsection中のsubsubsection
  4. 他のsection中のsubsection中のsubsubsection

- [Beamer: Highlighting subsubsections in TOC](https://tex.stackexchange.com/questions/231128/beamer-highlighting-subsubsections-in-toc)
