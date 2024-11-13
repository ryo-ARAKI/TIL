# デフォルトのフォントサイズを変更する

以下をプリアンプルに書けばよい

```latex
\setbeamerfont{normal text}{size=\large}
\AtBeginDocument{\usebeamerfont{normal text}}
```

`\setbeamerfont{normal text}{size=\large}` だけでは反映されないらしい．

参考：[How to set a small default font size with beamer?](https://tex.stackexchange.com/a/658975)
