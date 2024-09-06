# Python の `venv` 仮想環境を設定し，自動で有効化/無効化する

※以下は， `bash` をログインシェル， `fish` をインタラクティブシェルとして使っている環境における設定である．
すなわち， `direnv` を `fish` で有効化しつつ， `venv` は `bash` で起動している．

1. `direnv` を導入して `fish` シェルで有効化する
   ```
   sudo apt install direnv
   echo 'eval "$(direnv hook fish)"' >> ~/.config/fish/config.fish
   ```
2. 作業するリポジトリで Python の `venv` 環境を `.venv/` に作成する
   ```
   cd /path/to/your/repository/
   python3 -m venv .venv
   ```
3. `venv` を `bash` で起動するよう設定し，その設定ファイルを `.gitignore` に追加する
   ```
   echo 'source .venv/bin/activate' > .envrc
   direnv allow
   echo -e '\n# Python venv\n.envrc' >> .gitignore
   ```
