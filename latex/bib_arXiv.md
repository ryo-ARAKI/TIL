# `.bib` ファイルでの arXiv の論文のフォーマット

以下に[Tanogami and Araki (2022)](https://arxiv.org/abs/2206.11163)の文献情報を `.bib` ファイルに登録する例を示す：

```bibtex
@article{Tanogami2023_information-thermodynamic,
  doi = {10.48550/ARXIV.2206.11163},
  url = {https://arxiv.org/abs/2206.11163},
  author = {Tanogami, Tomohiro and Araki, Ryo},
  keywords = {Statistical Mechanics (cond-mat.stat-mech), Fluid Dynamics (physics.flu-dyn), FOS: Physical sciences, FOS: Physical sciences},
  title = {Information-thermodynamic bound on information flow in turbulent cascade},
  publisher = {arXiv},
  journal = {arXiv preprint},
  year = {2022},
  archivePrefix = {arXiv},
  eprint = {2206.11163},
  primaryClass = {stat-mech}
}
```

- `journal` に `arXiv preprint` を指定する
- `archivePrefix` に `arXiv` を指定する
- `eprint` には原稿の管理番号（年月.通し番号の9桁の数字）を指定する
- `primaryClass` には原稿を投稿する際に指定した分野を挿入する

----

なお，arXiv の"Export Bibtex Citation"ボタンから出力した文献情報は

```bibtex
@misc{https://doi.org/10.48550/arxiv.2206.11163,
  doi = {10.48550/ARXIV.2206.11163},

  url = {https://arxiv.org/abs/2206.11163},

  author = {Tanogami, Tomohiro and Araki, Ryo},

  keywords = {Statistical Mechanics (cond-mat.stat-mech), Fluid Dynamics (physics.flu-dyn), FOS: Physical sciences, FOS: Physical sciences},

  title = {Information-Thermodynamic Bound on Information Flow in Turbulent Cascade},

  publisher = {arXiv},

  year = {2022},

  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

でありいくつかのフィールド（`journal`，`archivePrefix`，`primaryClass`，`eprint`）が抜けているし，空行が入っているのも気持ちが悪い．
Google Scholar で arXiv プレプリントの引用情報を BibTeX フォーマットで出力すると，

```bibtex
@article{tanogami2022information,
  title={Information-Thermodynamic Bound on Information Flow in Turbulent Cascade},
  author={Tanogami, Tomohiro and Araki, Ryo},
  journal={arXiv preprint arXiv:2206.11163},
  year={2022}
}
```

となり，きわめて簡潔なものとなる．
