# Python のパッケージを全て更新する

1. 古くなった（outdated）パッケージのリストを取得

```linux
pip3 list --outdated
```

2. それら全てを更新

```linux
pip3 list -o | cut -f1 -d' ' | tr " " "\n" | awk '{if(NR>=3)print)' | cut -d' ' -f1 | xargs -n1 pip3 install -U
```

- [How To Update All Python Packages](https://www.activestate.com/resources/quick-reads/how-to-update-all-python-packages/)
