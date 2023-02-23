# Matplotlib のカラーマップと同じ色を使う

まず， Pythonのスクリプト中で使用している色を記録する．

```python
import matplotlib

plasma = matplotlib.cm.get_cmap('plasma')

color = plasma(0.5)
print(color)
# (0.798216, 0.280197, 0.469538, 1.0)
```

- 参考：[Getting individual colors from a color map in matplotlib](https://stackoverflow.com/a/25408562)

このRGB値を使ってLaTeXで色を定義する．

```latex
\usepackage{xcolor}

\definecolor{plasma_color}{RGB}{0.798216, 0.280197, 0.469538}
```

- 参考：[Color RGB in LaTeX](https://tex.stackexchange.com/a/239463)
