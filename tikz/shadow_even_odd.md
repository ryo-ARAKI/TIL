# 図で強調したい領域以外に影をつける

`even odd` ルールを使うとよい．
例えば，下記のコードを実行すると[-3,3]×[-2,2]の領域の中心にある半径1の円 **以外** の部分に影がつく．

```latex
\fill[black,opacity=.2,even odd rule]
(-3, -2) rectangle (3, 2)  % Even
(0, 0) circle[radius=1];  % Odd
```

- 参考：[How to shade a region outside the sphere in Tikz](https://tex.stackexchange.com/a/227771)
