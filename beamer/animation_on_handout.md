# 図を入れ替えるなどのアニメーションを入れているとき， handout にもそれを反映する

```latex
\begin{frame}<handout:1-2>{Slide title}
  foo\onslide<all:2>bar
\end{frame}
```

のように書くと， handout でも 2 枚のスライドが作成される．

- 参考：[Beamer handout mode: explicitly printing "half-way" frames](https://tex.stackexchange.com/a/184136)
