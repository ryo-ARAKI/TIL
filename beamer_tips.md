# Beamer の Tips や備忘録

## 目次の表示を制御する

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

## `itemize` 環境にアニメーションをつける

```latex
\begin{itemize}
  \item hoge
  \pause
  \item huga
\end{itemize}
```

のようにするとレイアウトが崩れる場合がある．

```latex
\begin{itemize}
  \item hoge
  \item<2-> huga
\end{itemize}
```

のように書けばよい．

## 図を入れ替えるなどのアニメーションを入れているとき， `handout` にもそれを反映する

```latex
\begin{frame}<handout:1-2>{Slide title}
  foo\onslide<all:2>bar
\end{frame}
```

のように書くと， `handout` でも2枚のスライドが作成される．

- 参考：[Beamer handout mode: explicitly printing "half-way" frames](https://tex.stackexchange.com/a/184136)

## `itemize` 環境中で一部だけ異なるbulletを使う

プリアンプルで

```latex
\newenvironment{redenv}{\only{\setbeamercolor{local structure}{fg=red}}}{}
```

のように書き， `itemize` 環境中で次のようにすれば，一部だけbulletの色を変えることができる．

```latex
\begin{frame}
  \begin{itemize}
    \item An item
    \item<red@1-> An item with red bullet
\end{frame}
```

- 参考：[beamer: change individual bullet color in itemize list](https://tex.stackexchange.com/a/14366)
