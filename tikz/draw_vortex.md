# 渦を描く

以下のコマンドを定義しておき

```latex
\newcommand\spiral{}  % Just for safety so \def will not overwrite something
\def\spiral[#1](#2)(#3:#4:#5:#6){  % \spiral[draw options](placement)(end angle:revolutions:final radius:rotation angle)
  \pgfmathsetmacro{\domain}{pi*#3/180+#4*2*pi}
  \draw [
    #1,
    shift={(#2)},
    rotate=#6,
    domain=0:\domain,
    variable=\t,
    smooth,
    samples=int(\domain/0.08)
  ] plot ({\t r}: {#5*\t/\domain})
}
```

例えば `tikzpicture` 環境中で

```latex
\spiral[very thick](0,0)(0:3:1:0);
```

とすれば

- 座標 $(0,0)$
- 終点角度 $180$°
- 回転数 $3$
- 半径 $1$
- 図全体の回転 $180$°

の渦が描ける．

- 参考：[Spiral spring in TikZ](https://tex.stackexchange.com/questions/29147/spiral-spring-in-tikz)
