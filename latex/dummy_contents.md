# ダミー文章や図を挿入する

## 英語：[lipsum](https://www.ctan.org/pkg/lipsum)パッケージ

```latex
# preample
\usepackage{lipsum}

# document
\lipsum[1-3]
```

## 日本語：[bxjalipsum](https://github.com/zr-tex8r/BXjalipsum)パッケージ

```latex
# preample
\usepackage{bxjalipsum}

# document
\jalipsum{iroha}  # いろは
\jalipsum{jugemu}  # 寿限無
\jalipsum[1-33]{wagahai}  # 吾輩は猫である
\jalipsum[1-4]{preamble}  # 憲法前文
\jalipsum[1-4]{hatsukoi}  # 初恋
```

## 図：[mwe](https://www.ctan.org/pkg/mwe)パッケージ

```latex
\includegraphics[width=0.6\textwidth]{example-image}
\includegraphics[width=0.6\textwidth]{example-image-16x9}
```
