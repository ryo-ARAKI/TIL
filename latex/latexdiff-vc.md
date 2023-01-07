# `LaTeXdiff` と `git` を連携する

```bash
latexdiff-vc -e utf8 -t CFONT --flatten --math-markup=2 --git --force -r HEAD^ main.tex
```

で直前のコミットとの差分が `diff-[commit hash].tex` として出力される．

- `-e utf8` 文字エンコーディングの指定
- `-t CFONT` 差分表示の指定．デフォルトだと打ち消し線と下波線での表示になるが，やや見づらいのでこちらがおすすめ
- `--flatten` `input` などで読み込んでいる別の `.tex` ファイルを正しく制御するために必要
- `--math-markup=2` 数式の差分管理の「おおらかさ」の指定．ファイルの差分が大きく `diff.tex` がうまくコンパイルできない場合はこの数値を下げるとよい．
- `-r` 差分をとる先を指定．ここでは直前のコミットを指定しているが，他にもブランチ名やコミットハッシュなどを指定できる．

- 参考
  - [Overleaf: Using Latexdiff For Marking Changes To Tex Documents](https://www.overleaf.com/learn/latex/Articles/Using_Latexdiff_For_Marking_Changes_To_Tex_Documents)
  - [にっき ♪：latexdiff](<http://abenori.blogspot.com/2016/06/latexdiff.html>
  - [Git で管理している LaTeX の diff を pdf で見る(TeXLive2015 版)](https://nekketsuuu.github.io/entries/2017/01/27/latexdiff-vc.html)
