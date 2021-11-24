# あるGitリポジトリ中のサブディレクトリを新しいリポジトリとして切り出す

Disclaimer：下記の手順も完璧ではない．この操作をおこなうときは十分調べてから実施すること．

## 目標

下のような構成になっているGitリポジトリ

```bash
big_repository/
    .git/
    subdir/
    to_be_new_repository/
```

から  `to_be_new_repository/` を新しいGitリポジトリとして切り出し，

```bash
big_repository
    .git/
    subdir/
to_be_new_repository/
    .git/
```
のようにする．

## 手順

[参考文献1](https://docs.github.com/en/get-started/using-git/splitting-a-subfolder-out-into-a-new-repository)にしたがって作業する．

1. 新しいcloneを作成する．

   ```bash
   $ cd tmp_directory
   $ git clone https://github.com/username/big_repository
   $ cd big_repository
   ```

2. 切り出したいサブディレクトリのみの情報を抽出する．

   ```bash
   $ git filter-repo --path to_be_new_repository/ --path-rename to_be_new_repository/:
   ```

   によって `to_be_new_repository/` をルートディレクトリしてリポジトリが再構成される．

   - `filter-repo` コマンドは `git` に含まれていないので，

        ```bash
        $ pip install git-filter-repo
        ```

        でインストールする．
   - 上記のコマンドだと `to_be_new_repository/` が作成されて以降のコミット履歴しか抽出できない．例えばリポジトリを分割するにあたって

        ```bash
        $ mv old_subdirectory to_be_new_repository
        $ mv some_dir/*.py to_be_new_repository/
        ```

        のようにファイル整理をしていた場合，この方法では履歴を引き継げない．このときは

        ```bash
        $ git filter-repo --path to_be_new_repository/ --path old_subdirectory/ --path some_dir/ --path-rename to_be_new_repository/:
        ```

        とすれば，

        1. 現在 `to_be_new_repository/` に含まれており
        2. `to_be_new_repository/` が作成される前から存在した

        ファイルの履歴も引き継ぐことができる．なお，より詳細に履歴を引き継ぐファイルを管理したい場合は[参考文献2](https://making.close.com/posts/splitting-sub-folders-out-into-new-git-repository)を参照せよ．

3. 新しいGitリポジトリ `new_repository` を作成し，リモートリポジトリのURLを取得する．
4. `filter-repo` でファイルを整理したリポジトリに新しく作成したリモートリポジトリを設定する．

   ```bash
   $ git remote add-url origin https://github.com/usename/new_repository.git
   ```

   - `git filter-repo` をおこなうと，もともと設定されていたリモートリポジトリの設定が消えてしまう．そのため， `git remote set-url` は上手くいかなかった．

5. 切り出したサブディレクトリの内容を新しいリポジトリにプッシュする．

    ```bash
    git switch -c add_files
    git push origin add_files
    ```

    - 規定のブランチ（ `master` か `main`）に直接はプッシュできない？
    - 上記のようにしても，履歴が完全に異なるためプルリクエストが作成できない（`add_files and master are entirely different commit histories` と表示される）ため，[参考文献3](https://stackoverflow.com/a/58657132)を参考に処理した．

        ```bash
        $ git switch add_files
        $ git branch master add_files -f
        $ git switch master
        $ git push origin master -f
        ```

      - この手順を実行すると，手順3で作成していた `README.md` や `.gitignore` が消えてしまうので注意．
      - 手順3の時点で何もファイルを作成しなければ大丈夫？それとも `initial commit` が存在する時点でダメ？（未検証）

6. もとのリポジトリから `to_be_new_repository` を削除する．

    ```bash
    $ cd move/to/new/clone/of/big_repository
    $ git switch -c delete_to_be_new_repository
    $ git rm -r to_be_new_repository
    $ git commit -m "delete `to_be_new_repository`"
    $ git push origin HEAD
    ```

    このプルリクエストをマージすれば作業は完了である．
    - 手順2で抽出した履歴を削除する方法がある？

## 参考

1. [Splitting a subfolder out into a new repository](https://docs.github.com/en/get-started/using-git/splitting-a-subfolder-out-into-a-new-repository)
2. [Splitting sub-folder(s) out into a new Git repository](https://making.close.com/posts/splitting-sub-folders-out-into-new-git-repository)
3. [Answer to: There isn't anything to compare. Nothing to compare, branches are entirely different commit histories](https://stackoverflow.com/a/58657132)
