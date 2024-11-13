# ファイル名にピリオドが含まれるファイルからモジュールを読み込む

例えば `./1.1_test.py` というファイルに記述された `test` モジュールを読み込むとき，

```python
import 1.1_test
```

のように書くとエラーとなる．
これはピリオドがついているとPythonのサブパッケージ構造とみなされるため．
これを回避するためには次のように書く：

```python
spec = importlib.util.spec_from_file_location(
    name="test",
    location="./1.1_test.py",
)
test = importlib.util.module_from_spec(spec)
spec.loader.exec_module(test)
```

## 参考

- [Stack Overflow: Import with dot name in python](https://stackoverflow.com/a/27189110)
