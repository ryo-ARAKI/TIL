# TIL

Memorandum of Today I Learned (in Japanese)

今日学んだこと（Today I Learned TIL）のメモ

## テンプレート/設定ファイル

<details>
<summary>テンプレート/設定ファイルのリスト</summary>

Gist で管理している各種設定ファイルやテンプレートのリンクをまとめる．

- [LaTeX template](https://gist.github.com/ryo-ARAKI/9aa9ce4f0fab42a758e1370ad1eb4487)
  - LaTeX のテンプレート
  - [latex_template.tex](https://gist.github.com/ryo-ARAKI/9aa9ce4f0fab42a758e1370ad1eb4487#file-latex_template-tex) ：和文のテンプレート
  - [beamer_template.tex](https://gist.github.com/ryo-ARAKI/9aa9ce4f0fab42a758e1370ad1eb4487#file-beamer_template-tex) ：スライドのテンプレート
  - [beamer_template_poster.tex](https://gist.github.com/ryo-ARAKI/9aa9ce4f0fab42a758e1370ad1eb4487#file-beamer_template_poster-tex) ：ポスターのテンプレート
  - [beamer_template_flash_talk.tex](https://gist.github.com/ryo-ARAKI/9aa9ce4f0fab42a758e1370ad1eb4487#file-beamer_template_flash_talk-tex) ：フラッシュトークのテンプレート
  - [standalone_figure.tex](https://gist.github.com/ryo-ARAKI/9aa9ce4f0fab42a758e1370ad1eb4487#file-standalone_figure-tex) ：TikZ を用いたスタンドアロン図のテンプレート
- [config.fish](https://gist.github.com/ryo-ARAKI/9d5e85d7be10863d515850b2ce2182e3)
  - [fish shell](https://fishshell.com/) の設定ファイル
- [LaTeX `.sty`](https://gist.github.com/ryo-ARAKI/c4f55e2c4c57a5997700160cc6ea55df)
  - LaTeX の設定ファイル
  - [mystyle.sty](https://gist.github.com/ryo-ARAKI/c4f55e2c4c57a5997700160cc6ea55df#file-mystyle-sty)
  - [mystyle_jpn.sty](https://gist.github.com/ryo-ARAKI/c4f55e2c4c57a5997700160cc6ea55df#file-mystyle_jpn-sty) ：和文用設定ファイル
  - [mystyle_beamer.sty](https://gist.github.com/ryo-ARAKI/c4f55e2c4c57a5997700160cc6ea55df#file-mystyle_beamer-sty) ：Beamer 用設定ファイル
  - [mystyle_beamer_jpn.sty](https://gist.github.com/ryo-ARAKI/c4f55e2c4c57a5997700160cc6ea55df#file-mystyle_beamer_jpn-sty) ：和文 Beamer 用設定ファイル
  - [mystyle_biblatex.sty](https://gist.github.com/ryo-ARAKI/c4f55e2c4c57a5997700160cc6ea55df#file-mystyle_biblatex-sty) ： BibLaTeX 用設定ファイル
  - [.latexmkrc_revtex](https://gist.github.com/ryo-ARAKI/8a256ef600325b0344bbc3990818b691#file-latexmkrc_revtex) ：欧文コンパイル用設定ファイル
  - [.latexmkrc_uplatex](https://gist.github.com/ryo-ARAKI/8a256ef600325b0344bbc3990818b691#file-latexmkrc_uplatex) ：和文コンパイル用設定ファイル
- [.screenrc](https://gist.github.com/ryo-ARAKI/07923755368e1f4ee0f67778a1cf2bca)
  - ターミナルエミュレーションソフトである screen の設定ファイル
- [starship.toml](https://gist.github.com/ryo-ARAKI/48a11585299f9032fa4bda60c9bba593)
  - ターミナルのプロンプトを装飾してくれる [Starship](https://starship.rs/) の設定ファイル
- [config](https://gist.github.com/ryo-ARAKI/f4031daf4d4c388838b123705aee8893)
  - ターミナルエミュレータである [Terminator](https://gnome-terminator.org/) の設定ファイル
- [.vimrc](https://gist.github.com/ryo-ARAKI/a9e64763c1f7d6eb1e210cb13388fd43)
  - vim の設定ファイル
- [.xbindkeysrc](https://gist.github.com/ryo-ARAKI/b17adac7419087a8ae821ebd1b30cd81)
  - 多ボタンマウスの Linux 用設定ファイル
  - Logitech MX Master 2S

</details>

## [Beamer](https://github.com/ryo-ARAKI/TIL/tree/master/beamer)

<details>
<summary>Beamerのtipsリスト</summary>

- [backup_slide.md](https://github.com/ryo-ARAKI/TIL/blob/master/beamer/backup_slide.md)
  - Beamerで総スライド番号に影響しない補遺スライドを作成する
- [bibliography_break_frame.md](https://github.com/ryo-ARAKI/TIL/blob/master/beamer/bibliography_break_frame.md)
  - Beamerで参考文献を出力する
- [change_default_font_size.md](https://github.com/ryo-ARAKI/TIL/blob/master/beamer/change_default_font_size.md)
  - デフォルトのフォントサイズを変更する
- [handout_with_complex_animation.md](https://github.com/ryo-ARAKI/TIL/blob/master/beamer/handout_with_complex_animation.md)
  - アニメーションを handout に反映する
- [hfill_in_frametitle.md](https://github.com/ryo-ARAKI/TIL/blob/master/beamer/hfill_in_frametitle.md)
  - Frametitle 中で右揃えする
- [itemize_animation.md](https://github.com/ryo-ARAKI/TIL/blob/master/beamer/itemize_animation.md)
  - `itemize` 環境にアニメーションをつける
- [itemize_temporarily_different_bullet.md](https://github.com/ryo-ARAKI/TIL/blob/master/beamer/itemize_temporarily_different_bullet.md)
  - `itemize` 環境中で一部だけ異なる bullet を使う
- [toc_customise.md](https://github.com/ryo-ARAKI/TIL/blob/master/beamer/toc_customise.md)
  - 目次の表示を制御する

</details>

## [Fortran](https://github.com/ryo-ARAKI/TIL/tree/master/fortran)

<details>
<summary>Fortranのtipsリスト</summary>

- [f2py.f90](https://github.com/ryo-ARAKI/TIL/blob/master/fortran/f2py.f90)と[f2py.py](https://github.com/ryo-ARAKI/TIL/blob/master/fortran/f2py.py)
  - Fortran と Python を連携する F2PY のサンプルプログラム
- [ifdef.f90](https://github.com/ryo-ARAKI/TIL/blob/master/fortran/ifdef.f90)
  - `#ifdef` フラグのサンプルプログラム

</details>

## [Git](https://github.com/ryo-ARAKI/TIL/tree/master/git)

<details>
<summary>Gitのtipsリスト</summary>

- [extract_subdirectory_as_new_repository.md](https://github.com/ryo-ARAKI/TIL/blob/master/git/extract_subdirectory_as_new_repository.md)
  - ある Git リポジトリ中のサブディレクトリを新しいリポジトリとして切り出す
- [rename_remote_branch.md](https://github.com/ryo-ARAKI/TIL/blob/master/git/rename_remote_branch.md)
  - Remote branch の名前を変える

</details>

## [Gnuplot](https://github.com/ryo-ARAKI/TIL/tree/master/gnuplot)

<details>
<summary>Gnuplotのtipsリスト</summary>

- [decimate_data.md](https://github.com/ryo-ARAKI/TIL/blob/master/gnuplot/decimate_data.md)
  - データを間引いて描画する
- [do_not_plot_0_data.md](https://github.com/ryo-ARAKI/TIL/blob/master/gnuplot/do_not_plot_0_data.md)
  - y=0 を描画しない
- [install_without_sudo.md](https://github.com/ryo-ARAKI/TIL/blob/master/gnuplot/install_without_sudo.md)
  - サーバに sudo 権限無しで gnuplot ver5.2.8 をインストールする
- [keep_plot_generated_by_gp_script.md](https://github.com/ryo-ARAKI/TIL/blob/master/gnuplot/keep_plot_generated_by_gp_script.md)
  - `.gp` スクリプトで描画したグラフを表示し続ける
- [plot_sum_of_multiple_columns.md](https://github.com/ryo-ARAKI/TIL/blob/master/gnuplot/plot_sum_of_multiple_columns.md)
  - 複数の列データの和を描画する
- [print_key_in_front.md](https://github.com/ryo-ARAKI/TIL/blob/master/gnuplot/print_key_in_front.md)
  - 凡例を前面に出力する
- [set_plot_range.md](https://github.com/ryo-ARAKI/TIL/blob/master/gnuplot/set_plot_range.md)
  - データの描画範囲を指定する

</details>

## [Julia](https://github.com/ryo-ARAKI/TIL/tree/master/julia)

<details>
<summary>Juliaのtipsリスト</summary>

- [package_list_for_physics_simulation.md](https://github.com/ryo-ARAKI/TIL/blob/master/julia/package_list_for_physics_simulation.md)
  - 物理シミュレーション/数値計算に役立つ Julia のパッケージリスト
- [performance_improvement.md](https://github.com/ryo-ARAKI/TIL/blob/master/julia/performance_improvement.md)
  - Juilaで実装したコードを高速化する方法
- [Unitful.jl](https://github.com/ryo-ARAKI/TIL/blob/master/julia/Unitful.jl)
  - `Unitful` パッケージを使った単位つき数値の計算のサンプルプログラム

</details>

## [LaTeX](https://github.com/ryo-ARAKI/TIL/tree/master/latex)

<details>
<summary>LaTeXのtipsリスト</summary>

- [aligned_equations_breakline.md](https://github.com/ryo-ARAKI/TIL/blob/master/latex/aligned_equations_breakline.md)
  - `aligned` 環境下で長い方程式を改行する
- [arxiv_with_template.md](https://github.com/ryo-ARAKI/TIL/blob/master/latex/arxiv_with_template.md)
  - いろいろな論文雑誌のテンプレートを使って arXiv にプレプリントを投稿する際の注意点
- [bib_arXiv.md](https://github.com/ryo-ARAKI/TIL/blob/master/latex/bib_arXiv.md)
  - `.bib` ファイルでの arXiv の論文のフォーマット
- [bib_check_lacking_field.md](https://github.com/ryo-ARAKI/TIL/blob/master/latex/bib_check_lacking_field.md)
  - `.bib` ファイルの必須フィールドの抜けを確認する
- [biblatex_submit_to_APS.md](https://github.com/ryo-ARAKI/TIL/blob/master/latex/biblatex_submit_to_APS.md)
  - REVTeX + BibLaTeX で参考文献を管理している論文を APS に投稿する
- [biblatex_suppress_issue_inside_parthensis.md](https://github.com/ryo-ARAKI/TIL/blob/master/latex/biblatex_suppress_issue_inside_parthensis.md)
  - BibLaTeX で出版年の括弧に `issue` の情報が入ってしまうのを抑制する
- [dummy_contents.md](https://github.com/ryo-ARAKI/TIL/blob/master/latex/dummy_contents.md)
  - ダミー文章や図を挿入する
- [empheq_single_equation_number.md](https://github.com/ryo-ARAKI/TIL/blob/master/latex/empheq_single_equation_number.md)
  - `empheq` 環境下で数式番号をまとめる
- [eqref_refer.md](https://github.com/ryo-ARAKI/TIL/blob/master/latex/eqref_refer.md)
  - `\eqref` で数式を参照する
- [footnote_inside_caption.md](https://github.com/ryo-ARAKI/TIL/blob/master/latex/footnote_inside_caption.md)
  - Caption中に `\footnote` を挿入する
- [holizontal_line_for_document_width.md](https://github.com/ryo-ARAKI/TIL/blob/master/latex/holizontal_line_for_document_width.md)
  - 文章幅と同じ長さの横線を引く
- [hyperref_setup.md](https://github.com/ryo-ARAKI/TIL/blob/master/latex/hyperref_setup.md)
  - `hyperref` パッケージの設定
- [itemize_align_inside.md](https://github.com/ryo-ARAKI/TIL/blob/master/latex/itemize_align_inside.md)
  - `itemize` 環境内でテキストを揃える
- [latexdiff-vc.md](https://github.com/ryo-ARAKI/TIL/blob/master/latex/latexdiff-vc.md)
  - LaTeXdiff と git を連携する
- [matplotlib_colour.md](https://github.com/ryo-ARAKI/TIL/blob/master/latex/matplotlib_colour.md)
  - Matplotlib のカラーマップと同じ色を使う
- [overflow_numbering_suppress.md](https://github.com/ryo-ARAKI/TIL/blob/master/latex/overflow_numbering_suppress.md)
  - footnote 番号（アルファベット）や `\subfloat` の図番号のオーバーフローを抑制する
- [revtex_preamble.md](https://github.com/ryo-ARAKI/TIL/blob/master/latex/revtex_preamble.md)
  - REVTeXなど論文執筆時の `.tex` テンプレートに追加するパッケージや設定
- [siunitx.md](https://github.com/ryo-ARAKI/TIL/blob/master/latex/siunitx.md)
  - siunitx を使った単位付き数値を math 環境で使う際の最適解
- [super_sub_script_in_text.md](https://github.com/ryo-ARAKI/TIL/blob/master/latex/super_sub_script_in_text.md)
  - Math モード以外で上付き（下付き）文字を使う
- [texlive_clean_install.md](https://github.com/ryo-ARAKI/TIL/blob/master/latex/texlive_clean_install.md)
  - TeXLive をクリーンインストールする手順
- [toc_correct_pagenumber_and_link.md](https://github.com/ryo-ARAKI/TIL/blob/master/latex/toc_correct_pagenumber_and_link.md)
  - 手動で目次に追加する項目に正しくページ番号とリンクを対応づける
- [transpose_symbol.md](https://github.com/ryo-ARAKI/TIL/blob/master/latex/transpose_symbol.md)
  - 行列，ベクトルの転置（transpose）をどう表記するか？
- [underbrace_breakline.md](https://github.com/ryo-ARAKI/TIL/blob/master/latex/underbrace_breakline.md)
  - `underbrace` 環境中で改行する
- [underbrace_fix.md](https://github.com/ryo-ARAKI/TIL/blob/master/latex/underbrace_fix.md)
  - `\underbrace` の表示がおかしい
- [underline_breakline.md](https://github.com/ryo-ARAKI/TIL/blob/master/latex/underline_breakline.md)
  - `\underline` 環境中で改行する

</details>

## [Linux](https://github.com/ryo-ARAKI/TIL/tree/master/linux)

<details>
<summary>Linuxのtipsリスト</summary>

- [command_cheatsheet.md](https://github.com/ryo-ARAKI/TIL/blob/master/linux/command_cheatsheet.md)
  - Linux の（やや複雑な）コマンドチートシート
- [fish_add_remove_path.md](https://github.com/ryo-ARAKI/TIL/blob/master/linux/fish_add_remove_path.md)
  - fish shell における永続的な `PATH` の追加/削除
- [gnome_shell_extensions.md](https://github.com/ryo-ARAKI/TIL/blob/master/linux/gnome_shell_extensions.md)
  - GNOME shell extensionsのリスト
- [shell_interactive.md](https://github.com/ryo-ARAKI/TIL/blob/master/linux/shell_interactive.md)
  - シェルスクリプトにおける Yes/No の選択に応じた対話的実行
- [shell_iteration.md](https://github.com/ryo-ARAKI/TIL/blob/master/linux/shell_iteration.md)
  - シェルスクリプトにおける複数のファイルに対する繰り返し処理

</details>

## [Python](https://github.com/ryo-ARAKI/TIL/tree/master/python)

<details>
<summary>Pythonのtipsリスト</summary>

- [lineplot_with_arrow_annotation.py](https://github.com/ryo-ARAKI/TIL/blob/master/python/lineplot_with_arrow_annotation.py)
  - Matplotlib の `plt.plot` に矢印のアノーテーションをつけるサンプルプログラム
- [maintain_same_margin_for_different_label.md](https://github.com/ryo-ARAKI/TIL/blob/master/python/maintain_same_margin_for_different_label.md)
  - 異なる軸ラベルに対して同一のプロット領域を確保する
- [matplotlib_bool_mask.py](https://github.com/ryo-ARAKI/TIL/blob/master/python/matplotlib_bool_mask.py)
  - Matplotlib の `plot` で，boolean array を用いてグラフの一部だけを強調するサンプルプログラム
- [matplotlib_latex.py](https://github.com/ryo-ARAKI/TIL/blob/master/python/matplotlib_latex.py)
  - Matplotlib で LaTeX 書式を使うサンプルプログラム
- [matplotlib_share_x_axis.py](https://github.com/ryo-ARAKI/TIL/blob/master/python/matplotlib_share_x_axis.py)
  - Matplotlib で異なるスケールのデータを$x$軸を共有してプロットするサンプルプログラム
- [matplotlib_ticks_position.py](https://github.com/ryo-ARAKI/TIL/blob/master/python/matplotlib_ticks_position.py)
  - Matplotlib で軸の `ticks` 位置を調整するサンプルプログラム
- [numerical_sequence_with_white_space.md](https://github.com/ryo-ARAKI/TIL/blob/master/python/numerical_sequence_with_white_space.md)
  - 数列を空白区切りで出力する
- [scatter_plot_with_raster.md](https://github.com/ryo-ARAKI/TIL/blob/master/python/scatter_plot_with_raster.md)
  - Scatter プロットの scatter 部分のみをラスタライズして高速化する

</details>

## [TikZ](https://github.com/ryo-ARAKI/TIL/tree/master/tikz)

<details>
<summary>TikZのtipsリスト</summary>

- [bezier_curve.md](https://github.com/ryo-ARAKI/TIL/blob/master/tikz/bezier_curve.md)
  - Bézier曲線 control points で制御する
- [draw_vortex.md](https://github.com/ryo-ARAKI/TIL/blob/master/tikz/draw_vortex.md)
  - 渦を描く
- [shadow_even_odd.md](https://github.com/ryo-ARAKI/TIL/blob/master/tikz/shadow_even_odd.md)
  - 図で強調したい領域**以外** に影をつける
- [tikz_tutorial.md](https://github.com/ryo-ARAKI/TIL/blob/master/tikz/tikz_tutorial.md)
  - TikZ のチュートリアル
- [use_colon.md](https://github.com/ryo-ARAKI/TIL/blob/master/tikz/use_colon.md)
  - `tikzpicture` 環境中でコロン記号を使う

</details>

## To Be Added

<details>
<summary>今後追加したいtips</summary>

- HDF ファイル
  - Fortran90 から HDF ファイル形式への書き込み，読み取り方法
  - HDF ファイルを ParaView から読み込む方法
- LaTeX
  - 卒論/修論テンプレートで工夫した点
  - 博士論文のテンプレートで工夫した点
  - 上記テンプレートで工夫した点
- Python
  - 解析コードで工夫した点
- Julia
  - 解析コードで工夫した点

</details>
