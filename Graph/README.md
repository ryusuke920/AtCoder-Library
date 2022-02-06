# AtCoder-Library

[AtCoder](https://atcoder.jp/) のライブラリを保管しています。

(*stores AtCoder-Library.*)  

## Graph
|File Name|Algorithm|Explanation|
|:--:|:--:|:--:|
|[bellman_ford.py](bellman_ford.py)|ベルマンフォード法|負辺を含む単一最短経路問題を求める。負閉路の検出も可能。|
|[dijkstra.py](dijksra.py)|ダイクストラ法|単一頂点からの最小距離を求める。|
|[EulerTourpy](EulerTour.py)|オイラーツアー|根付きを根からDFSし根に戻ってくる行きと戻りの経路を1次元のテーブルに記録したもの。同時に、辿る際に以下のような情報を記録し、それらに対してRMQやRSQを適応することで木に対するいくつかのクエリを高速に行える。|
|[Kruskal.py](Kruskal.py)|クラスカル法|最小全域木を求める。Union-Findを用いてグラフの連結判定を行う。|
|[LowestCommonAncestor.py](LowestCommonAncestor.py)|最小共通祖先|ある２つの頂点に対して、その両方を自身以下に持つ頂点のうち、最も低い位置にある頂点を求める|
|[Prim.py](Prim.py)|プリム法|最小全域木を求める。訪れた頂点数をカウントしながら求める。|
|[Strongly Connected Component](Strongly Connected Component)|強連結成分分解|有向グラフにおいて、互いに行き来が可能な頂点の集合を求める。|
|[TopologicalSort.py](TopologicalSort.py)|トポロジカルソート|有向非巡回グラフの各頂点を順序付けして、どの頂点もその出力辺の先の頂点より前に来るように並べる。DAG(Directed Acyclic Graph)との相性が良い|
|[warshall_floyd.py](warshall_floyd.py)|ワーシャルフロイド法|O(N^3)かかってしまうため、頂点数が少ない時に有効|