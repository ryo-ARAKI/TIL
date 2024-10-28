# 特定の行に VSCode の自動整形を作用させない

例えばローカルのパッケージをインポートするときは

```python
sys.path.append('/path/to/dir/')
import local_package
```

のように書く必要があるが，ファイル保存時に PEP8 などのコーディング規約を適用する設定にしていると行の順序が入れ替わってしまう．
このとき，以下のように `# nopep8` というコメントをつけるとその行にコーディング規約が矯正されなくなる：

```python
sys.path.append('/path/to/dir/')  # nopep8
import local_package  # nopep8
```

## 参考

- [Stack Overflow: Allow statements before imports with Visual Studio Code and autopep8](https://stackoverflow.com/a/57067521)
