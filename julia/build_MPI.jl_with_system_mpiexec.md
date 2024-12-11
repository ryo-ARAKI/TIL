# `MPI.jl` をシステムの `mpiexec` でビルドする

以下のように「普通に」 `MPI.jl` を導入すると，システムにインストールされている `mpiexec` と異なるものでビルドされる．
そのため，実行してもうまくいかない．

```bash
$ julia
(@v1.11) pkg> add MPI
julia> using MPI
$ mpiexec -n 4 julia 01-hello.jl  # https://juliaparallel.org/MPI.jl/stable/examples/01-hello/ にある練習プログラム
┌ Warning:     You appear to have run julia under a different `mpiexec` than the one used by MPI.jl.
│     See the documentation for details.
└ @ MPI ~/.julia/packages/MPI/TKXAj/src/environment.jl:26
Hello world, I am rank 0 of 1
（省略）
```

これは以下のように確認できる：

```bash
julia> println(MPI.mpiexec())
/home/username/.julia/artifacts/xxxxxx/bin/mpiexec  # こんな感じのmpiexecへのパス
$ which mpiexec
/usr/bin/mpiexec  # ≠ println(MPI.mpiexec())
```

解決策として `mpiexecjl` をインストールする方法がある（参考：[Julia wrapper for `mpiexec`](https://juliaparallel.org/MPI.jl/stable/usage/#Julia-wrapper-for-mpiexec)）：

```bash
$ julia
julia> using MPI
julia> MPI.install_mpiexecjl()
$ /path/to/mpiexecjl -n 4 julia 01-hello.jl
Hello world, I am rank 3 of 4
Hello world, I am rank 0 of 4
Hello world, I am rank 1 of 4
Hello world, I am rank 2 of 4
```

しかしここではシステムの `mpiexec` で `MPI.jl` をビルドしたい．
以下のようにする：

```bash
$ julia
(@v1.11) pkg> add MPIPreferences
julia> using MPIPreferences
julia> MPIPreferences.use_system_binary()  # システムにインストールされているMPIを探す
┌ Info: MPI implementation identified
（略）
└   abi = "OpenMPI"
┌ Info: MPIPreferences changed
（略）
└   preloads_env_switch = nothing
julia> using Pkg
julia> Pkg.build("MPI"; verbose=true)  # MPI.jlをシステムのMPIで再ビルドする
julia> exit()  # 一度REPLを立ち上げ直す
$ julia
julia> using MPI
julia> println(MPI.mpiexec())
`mpiexec`
shell> which mpiexec
/usr/bin/mpiexec  # = println(MPI.mpiexec())
$ mpiexec -n 4 julia 01-hello.jl  # システムの `mpiexec` で実行できる！
Hello world, I am rank 0 of 4
Hello world, I am rank 3 of 4
Hello world, I am rank 1 of 4
Hello world, I am rank 2 of 4
```

スパコンで `MPI.jl` を使いたい場合も同様にすればよい．
例えば使用するノードの種類ごとにモジュールで環境が準備されているときは，使いたいモジュールをロードしてから上記の手順を実行すればよい．
