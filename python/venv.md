# Python の `venv` 仮想環境を設定し，自動で有効化/無効化する

1. `direnv` を導入し，シェルで有効化する
   ```
   sudo apt install direnv
   echo 'eval "$(direnv hook bash)"' >> ~/.bashrc
   source ~/.bashrc
   ```
2. 作業するリポジトリで `direnv` を設定し，設定ファイルを `.gitignore` に記述する
   ```
   cd /path/to/your/repository/
   echo 'source .venv/bin/activate' > .envrc
   echo '.envrc' >> .gitignore
   ```
3. Python の `venv` 環境を `.venv/` に作成する
   ```
   python3 -m venv .venv
   ```
