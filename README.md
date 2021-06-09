# AtCoder-Library
基本自作（基本なので例外もあります）のAtCoderのライブラリを保管しています。  
高速化に成功したアルゴリズムや理解して次回以降は  
0から書くと時間のかかるアルゴリズムの大枠などをまとめています。

## BFS
|コード名|アルゴリズム|用途 ・ 説明|
|:--:|:--:|:--:|
|BreadthFirstSearch.py|幅優先探索|迷路の最短経路を考える問題の時などに役に立つ|

## BinarySearch
|コード名|アルゴリズム|用途 ・ 説明|
|:--:|:--:|:--:|
|BinarySearch.py|二分探索|O(logN)で行えるのでとても高速|
|MegurusikiBinarySearch.py|二分探索|O(logN)で行えるのでとても高速, めぐる式二分探索はとても有名だが、使いこなせていない|

## Bisect
|コード名|アルゴリズム|用途 ・ 説明|
|:--:|:--:|:--:|
|kLessThanBisect.py|二分探索|配列Aの中のうち、k未満の個数と終わりの0indexを返すライブラリ|
|kMoreBisect.py|二分探索|配列Aの中のうち、kより大きいものの個数と始まりの0indexを返すライブラリ|
|kOrLessThanBisect.py|二分探索|配列Aの中のうち、k以下の個数と終わりの0indexを返すライブラリ|
|kOrMoreBisect.py|二分探索|配列Aの中のうち、k以上の個数と始まりの0indexを返すライブラリ|

## BIT
|コード名|アルゴリズム|用途 ・ 説明|
|:--:|:--:|:--:|
|BinaryIndexedTree.py|転倒数|転倒数を求められる|

## BitSearch
|コード名|アルゴリズム|用途 ・ 説明|
|:--:|:--:|:--:|
|BitSearch.py|Bit全探索|スイッチの ON / OFF 問題などに使える  計算量は O(2 ^ N)|

## CoordinateCompression
|コード名|アルゴリズム|用途 ・ 説明|
|:--:|:--:|:--:|
|CC.py|座標圧縮|配列の数値を昇順に順位付けする|

## DFS
|コード名|アルゴリズム|用途 ・ 説明|
|:--:|:--:|:--:|
|DepthFirstSearch.py|深さ優先探索|辺を辿っていく問題などの時に役に立つ|

## Dijkstra
|コード名|アルゴリズム|用途 ・ 説明|
|:--:|:--:|:--:|
|dijkstra.py|ダイクストラ法|ある頂点からの最小距離を求める|

## ExtendedEuclidean
|コード名|アルゴリズム|用途 ・ 説明|
|:--:|:--:|:--:|
|ExtGCD.py|拡張ユークリッドの互除法|ap + bq = d := gcd(a, b)となる (p, q, d) を返す|

## LongestCommonSubsequence(LCS)
|コード名|アルゴリズム|用途 ・ 説明|
|:--:|:--:|:--:|
|LCS.py|最長共通部分文字列|配列の最長共通部分列を出力してくれる|

## LongestIncreasingSubsequence(LIS)
|コード名|アルゴリズム|用途 ・ 説明|
|:--:|:--:|:--:|
|LIS.py|最長増加部分列|配列の最長増加列を出力してくれる|

## MathLibrary
|コード名|アルゴリズム|用途 ・ 説明|
|:--:|:--:|:--:|
|BinaryToDecimal.py|2進数 -> 10進数への変換|2進数を10進数に変換してくれる|
|DecimalToBinary.py|10進数 -> 2進数への変換|10進数を2進数に変換してくれる|
|DigitSum_1.py|桁和(1)|intのまま桁和を求められる|
|DigitSum_2.py|桁和(2)|strに変換した後に桁和を求められる|
|divisor.py|約数列挙|約数の列挙を行ってくれる|
|FromFloatToInt.py|float -> int|floatの誤差計算を防ぐためにintに変換して計算する|
|factorization.py|素因数分解|素因数分解を行ってくれる|
|PrimaryCheck.py|素数判定|その数が素数かどうかの判定を行ってくれる  一般的には十分高速だが, 競プロ界隈だと遅い|
|SieveOfEratosthenes_1.py|エラトステネスの篩 (Ver.1) |O(√N)よりも高速に素数を列挙してくれる （緑Diff以上になってくると使用するタイミングが出てくる）|
|SieveOfEratosthenes_2.py|エラトステネスの篩 (Ver.2) |Ver.1 の時よりも高速に素数を列挙することができる|
|XorToN_1.py|０〜NまでのXORをとる(Ver.1)|計算量はO(logN)|
|XorToN_2.py|０〜NまでのXORをとる(Ver.2)|Ver.1よりも高速に処理する, 計算量はO(1)|
|CumulativeSum.py|累積和|累積和を行ってくれる|
|MaxCumulativeSum.py|区間累積和の最大・最小問題|区間累積和の最大・最小を求められる|
|nCk.py|combinationの計算|nCkの計算を高速に行える, 計算量はO(K)|
|nCk_2.py|combinationの計算|nCk.pyのpowを最後に持ってきたから高速?, 計算量はO(K)|

## OtherLibrary
|コード名|アルゴリズム|用途 ・ 説明|
|:--:|:--:|:--:|
|debug.py|デバッグ用のprint出力|これを出力しても標準エラー出力になるので、ジャッジに反映されない|

## RunLengthEncoding
|コード名|アルゴリズム|用途 ・ 説明|
|:--:|:--:|:--:|
|RLE.py|ランレングス圧縮|２種類くらいのランダム文字列を何の文字が何連続で出てきたかを出力してくれる|

## SCC
|コード名|アルゴリズム|用途 ・ 説明|
|:--:|:--:|:--:|
|SCC.py|強連結成分分解(Strongly Connevted Component)|閉路検出を行ってくれる|

## SegmentTree
|コード名|アルゴリズム|用途 ・ 説明|
|:--:|:--:|:--:|
|SegTree.py|セグメントツリー|区間に対して色々なことができる|
|LazySegTree.py|遅延評価セグメントツリー|区間全体に対して色々なことができる|

## UnionFindTree
|コード名|アルゴリズム|用途 ・ 説明|
|:--:|:--:|:--:|
|UnionFind.py|素集合に分割するアルゴリズム|まだ使用しているのみで, 具体的な構造はわかっていない|
