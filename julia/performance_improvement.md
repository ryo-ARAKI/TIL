# Juilaで実装したコードを高速化する方法

1. 公式ドキュメントの[Performance Tips](https://docs.julialang.org/en/v1/manual/performance-tips/)を読んで型安定やメモリアクセスを改善する．
2. [BenchmarkTools.jl](https://juliaci.github.io/BenchmarkTools.jl/stable/)パッケージや[Profile](https://docs.julialang.org/en/v1/manual/profile/#Profiling)モジュールでホットスポットを見つける．
3. [@threds](https://docs.julialang.org/en/v1/base/multi-threading/)マクロや[FLoops.jl](https://github.com/JuliaFolds/FLoops.jl)パッケージの `@floop` マクロでスレッド並列を試す．
4. [LoopVectorization](https://github.com/JuliaSIMD/LoopVectorization.jl)パッケージの `@turbo` マクロや[@simd](https://docs.julialang.org/en/v1/base/base/#Base.SimdLoop.@simd)でSIMD化を試す．ただしメモリの扱いには注意する．
5. [MPI.jl](https://juliaparallel.org/MPI.jl/stable/)や[Distributed.jl](https://github.com/JuliaLang/Distributed.jl)でプロセス並列化を実装する．
   - この二つの差はよく分からない．参照：[Distributed.jl vs MPI.jl](https://discourse.julialang.org/t/distributed-jl-vs-mpi-jl/71315)

また，和書なら

- 進藤，佐藤「1から始めるJuliaプログラミング」，コロナ社（2020）の4章「Juliaの高速化」
- 後藤「実践Julia入門」，技術評論社（2023）の9章「平行・並列処理」

を参照せよ．
