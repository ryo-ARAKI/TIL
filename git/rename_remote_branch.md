# Remote branch の名前を変える

- 参考：[How To Rename a Local and Remote Git Branch](https://linuxize.com/post/how-to-rename-local-and-remote-git-branch/)

- remote branchを `<old_name>` から `<new_name>` に変更する

1. 名前を変えたいブランチに移動
   `$ git switch <old_name>`
2. ローカルブランチの名前を変更
   `$ git branch -m <new_name>`
3. 名前を変えたローカルブランチをリモートにプッシュし，追従するリモートブランチを新しくつくる
   `$ git push origin -u <new_name>`
4. 古い名前のリモートブランチを削除する
   `$ git push origin --delete <old_name>`

- `<old_name>` で出していたプルリクエストは閉じられるので， `<new_name>` で再度開く必要がある．
