# `siunitx`を使った単位付き数値を math 環境で使う際の最適解

```latex
\SI{9.81}{\meter/\second^2}
```

と同じ出力は

```latex
\(9.81\, \si{\meter/\second^2}\)
```

で得られる

- [The “correct” or recommended way of using siunitx in math mode](https://tex.stackexchange.com/questions/451967/the-correct-or-recommended-way-of-using-siunitx-in-math-mode)
