# Python のパッケージを全て更新する

1. 古くなった（outdated）パッケージのリストを取得

```linux
pip3 list --outdated
```

2. それら全てを更新

```linux
pip3 list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U
```

上記のコマンドでエラーが出るようになった．

```
ERROR: List format 'freeze' can not be used with the --outdated option.
Defaulting to user installation because normal site-packages is not writeable
ERROR: You must give at least one requirement to install (see "pip help install")
```

`--format=freeze` を外せばよい？

