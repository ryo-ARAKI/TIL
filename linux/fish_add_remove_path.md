# fish shell における永続的な `PATH` の追加/削除

## `PATH` の追加

```linux
set -U fish_user_paths /usr/local/bin $fish_user_paths
```

- [fish-shell 3.1.2 documentation:PATH](https://fishshell.com/docs/current/tutorial.html#path)

## `PATH` の削除

```linux
echo $fish_user_paths | tr " " "\n" | nl
set --erase --universal fish_user_paths[hoge]
```

- [How to remove a path from \$PATH variable in fish?](https://superuser.com/a/1091983)
- `echo $fish_user_paths | tr " " "\n" | nl`
  - `$PATH` を順番に表示する
- `set --erase --universal fish_user_paths[hoge]`
  - `hoge` 番の `$PATH` を削除する
