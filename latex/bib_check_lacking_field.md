# `.bib` ファイルの必須フィールドの抜けを確認する

`biber` に `-V` （`--validate-datamodel`）オプションをつける．
不足している/データ型（`@article` など）に存在しないフィールドの情報が `.bbl` ファイルに

```latex
\warn{\item Datamodel: Entry 'key' (./bibliography.bib): Missing mandatory field 'journaltitle'}
```

のように出力される．

- `.bib` ファイルの文献種別必須フィールドについては，例えば[Bibtex Entry Types, Field Types and Usage Hints](https://www.openoffice.org/bibliographic/bibtex-defs.html)を参照せよ
