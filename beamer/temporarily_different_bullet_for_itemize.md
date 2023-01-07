# `itemize` 環境中で一部だけ異なるbulletを使う

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
