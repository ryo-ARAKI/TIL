# `empheq` 環境下で数式番号をまとめる

- `empheq` 環境の `equation` オプションと `split` 環境を使う

```latex
\begin{empheq}[left={\vb*{f} = \empheqlbrack}, right=\empheqrbrack]{equation}
  \begin{split}
    -&\sin(x) \cos(y) \\
    +&\cos(x) \sin(y) \\
    &0
  \end{split}
\end{empheq}
```

- さらに複数ヶ所でalignしたいとき： `begin{alignedat}` 環境を使う

```latex
\begin{empheq}[left={\vb*{f} = \empheqlbrack}]{equation}\begin{alignedat}{3}
  &\qty[\pi R^2]^{-1} &\quad &r \le R \\
  &\quad 0 &\quad &\text{else}
\end{alignedat}\end{empheq}
```

- 参考：[Single equation number for `empheq`](https://tex.stackexchange.com/a/570363)
