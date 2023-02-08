# 渦を描く

プリアンブルに以下のコマンドを定義しておき

```latex
% Define vortex:
% \spiralclock[draw options](placement)(end angle:revolutions:final radius:rotation angle)
%   for clockwise vortex.
% \spiralcounterclock
%   for counter-clockwise vortex.
%
% https://tex.stackexchange.com/questions/29147/spiral-spring-in-tikz
\newcommand\spiralclock{}  % Just for safety so \def will not overwrite something
\newcommand\spiralcounterclock{}
\def\spiralclock[#1](#2)(#3:#4:#5:#6){
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
\def\spiralcounterclock[#1](#2)(#3:#4:#5:#6){
  \pgfmathsetmacro{\domain}{pi*#3/180+#4*2*pi}
  \draw [
    #1,
    shift={(#2)},
    rotate=#6,
    domain=0:\domain,
    variable=\t,
    smooth,
    samples=int(\domain/0.08)
  ] plot ({-\t r}: {#5*\t/\domain})
}
```

例えば `tikzpicture` 環境中で

```latex
\spiralclock[very thick](0,0)(0:3:1:0);
```

とすれば

- 座標 $(0,0)$
- 終点角度 $180$°
- 回転数 $3$
- 半径 $1$
- 図全体の回転 $180$°

の **時計回りの** 渦が描ける．
`spiralcounterclock` に同じパラメータを与えると **反時計回りの** 渦が描ける．

- 参考：[Spiral spring in TikZ](https://tex.stackexchange.com/questions/29147/spiral-spring-in-tikz)
