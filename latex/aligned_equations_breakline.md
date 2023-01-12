# `aligned` 環境下で長い方程式を改行する

- 統合を揃えつつ長い式を改行して適切にスペーシングするには `quad` を使う

```latex
\begin{empheq}{align}
  LHS of equation
    &= RHS of equation \\
    &\quad + Second line of RHS of equation
\end{empheq}
```

- 参考：[Spacing after equals sign in align](https://tex.stackexchange.com/a/212606)
