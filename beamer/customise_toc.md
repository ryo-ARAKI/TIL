# 目次の表示を制御する

- `\tableofcontents` に次のようなオプションを指定する

```latex
\tableofcontents[
  sectionstyle=show/shaded,
  subsectionstyle=show/show/shaded,
  subsubsectionstyle=show/show/show/shaded
]
```

- key は `show, shaded, hide` の 3 種類
- `sectionstyle`
  1. 現在の section
  2. それ以外の section
- `subsectionstyle`
  1. 現在の subsection
  2. 現在の section 中の他の subsection
  3. 他の section 中の subsection
- `subsubsectionstyle`

  1. 現在の subsubsection
  2. 現在の subsection 中の他の subsubsection
  3. 現在の section の他の subsection 中の subsubsection
  4. 他の section 中の subsection 中の subsubsection

- [Beamer: Highlighting subsubsections in TOC](https://tex.stackexchange.com/questions/231128/beamer-highlighting-subsubsections-in-toc)
