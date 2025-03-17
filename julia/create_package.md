# パッケージを作成する

1. GitHubで**空の**パッケージを作成する
   - `README.md`や`.gitignore`も作成しない
2. パッケージを作成したいディレクトリで

   ```bash
    $ julia
    julia> using PkgTemplates
    julia> t = Template(;user="user", authors=["AUTHOR Name"], dir="./", julia=v"1.11")
    julia> generate("package-name.jl", t)
   ```

   とする．
   ここで，`user`はGitHubのユーザ名，`authors`は開発者の名前，`julia`は使用したいJuliaのバージョンを指定する．
   これで，

   ```bash
   package-name.jl
   ├── LICENSE
   ├── Project.toml
   ├── README.md
   ├── src
   │  └── package-name.jl
   └── test
   └── runtests.jl
   ```

   のファイルが生成される．

3. 手順2で作成したローカルパッケージを手順1で作成したGitHubリポジトリに登録する

   ```bash
   cd package-name.jl
   git remote rm origin
   git remote add origin git@github.com:user/package-name.jl
   git push --set-upstream origin HEAD
   ```

## 参考文献

[永井 佑紀, 「Juliaではじめる数値計算入門」, 技術評論社 (2024)](https://gihyo.jp/book/2024/978-4-297-14128-8)のII-0
