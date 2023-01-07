# `itemize` 環境にアニメーションをつける

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
