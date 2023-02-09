# Bézier曲線を control points で制御する

プリアンブルに下記のように書いておき，

```latex
% To show curve controls, add 'show curve controls' to \draw comman
% cf. https://tex.stackexchange.com/a/255258
\usetikzlibrary{decorations.pathreplacing}
\tikzset{%
  show curve controls/.style={
    postaction={
      decoration={
        show path construction,
        curveto code={
          \draw [blue]
            (\tikzinputsegmentfirst) -- (\tikzinputsegmentsupporta)
            (\tikzinputsegmentlast) -- (\tikzinputsegmentsupportb);
          \fill [red, opacity=0.5]
            (\tikzinputsegmentsupporta) circle [radius=.5ex]
            (\tikzinputsegmentsupportb) circle [radius=.5ex];
        }
      },
      decorate
}}}
```

例えば次のコマンドを実行すると制御点つきでBézier曲線を描ける

```latex
% Energy spectrum
\draw[ultra thick, Navy, show curve controls] (0.2, 6.15)
  .. controls ++(170:-1) and ++(170:1) .. (1.5, 5.9)
  .. controls ++(170:-1) and ++(300:-1) .. (3.0, 5.0)
  .. controls ++(300:1) and ++(300:-1) .. (5.0, 1.5)
  .. controls ++(300:1) and ++(280:-1) .. (5.6, 0.0);
```

- 参考：[How does one pick control points to control Bézier curves in TikZ?](https://tex.stackexchange.com/a/255258)
