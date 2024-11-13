# BibLaTeXで出版年の括弧に `issue` の情報が入ってしまうのを抑制する

BibLaTeXでは `issue` ではなく `number` を使う．
プリアンプルに以下のようなマクロを書いて置換すれば良い．

```latex
\DeclareSourcemap{
  \maps[datatype=bibtex]{
    \map{
      \step[fieldsource=issue, match=\regexp{\A[0-9]+\Z}, final]
      \step[fieldset=number, origfieldval]
      \step[fieldset=issue, null]
    }
  }
}
```

- 参考
  - [biblatex - issue number of journal in date](https://tex.stackexchange.com/a/354762)
