# Python のパッケージを全て更新する

1. 古くなった（outdated）パッケージのリストを取得

```linux
pip3 list --outdated
```

2. それら全てを更新

```linux
pip3 list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U
```

