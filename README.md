# AtCoder-Library
基本自作（基本なので例外もあります）のAtCoderのライブラリを保管しています。  
高速化に成功したアルゴリズムや理解して次回以降は  
0から書くと時間のかかるアルゴリズムの大枠などをまとめています。

## BFS
|コード名|アルゴリズム|用途 ・ 説明|
|:--:|:--:|:--:|
|BreadthFirstSearch.py|幅優先探索|迷路の最短経路を考える問題の時などに役に立つ|

## BitSearch
|コード名|アルゴリズム|用途 ・ 説明|
|:--:|:--:|:--:|
|BitSearch.py|Bit全探索|スイッチの ON / OFF 問題などに使える  計算量は O(2 ^ N) |

## DFS
|コード名|アルゴリズム|用途 ・ 説明|
|:--:|:--:|:--:|
|DepthFirstSearch.py|深さ優先探索|辺を辿っていく問題などの時に役に立つ|

## MathLibrary
|コード名|アルゴリズム|用途 ・ 説明|
|:--:|:--:|:--:|
|BinaryIndexedTree.py|転倒数|転倒数を求められる|
|BinaryToDecimal.py|2進数 -> 10進数への変換|2進数を10進数に変換してくれる|
|DecimalToBinary.py|10進数 -> 2進数への変換|10進数を2進数に変換してくれる|
|DigitSum_1.py|桁和(1)|intのまま桁和を求められる|
|DigitSum_2.py|桁和(2)|strに変換した後に桁和を求められる|
|divisor.py|約数列挙|約数の列挙を行ってくれる|
|FromFloatToInt.py|float -> int|floatの誤差計算を防ぐためにintに変換して計算する|
|factorization.py|素因数分解|素因数分解を行ってくれる|
|PrimaryCheck.py|素数判定|その数が素数かどうかの判定を行ってくれる  一般的には十分高速だが, 競プロ界隈だと遅い|
|SieveOfEratosthenes_1|エラトステネスの篩 (Ver.1) |O(√N)よりも高速に素数を列挙してくれる （緑Diff以上になってくると使用するタイミングが出てくる）|
|SieveOfEratosthenes_1|エラトステネスの篩 (Ver.2) |Ver.1 の時よりも高速に素数を列挙することができる|
|CumulativeSum.py|累積和|累積和を行ってくれる|
|MaxCumulativeSum.py|区間累積和の最大・最小問題|区間累積和の最大・最小を求められる|
|nCk.py|combinationの計算|nCkの計算を高速に行える, 計算量はO(K)|

## LongestIncreasingSubsequence
|コード名|アルゴリズム|用途 ・ 説明|
|:--:|:--:|:--:|
|lis.py|最長増加部分列|配列の最長増加列を出力してくれる|

## RunLnegthEncoding
|コード名|アルゴリズム|用途 ・ 説明|
|:--:|:--:|:--:|
|rle.py|ランレングス圧縮|２種類くらいのランダム文字列を何の文字が何連続で出てきたかを出力してくれる|

## UnionFindTree
|コード名|アルゴリズム|用途 ・ 説明|
|:--:|:--:|:--:|
|UnionFind.py|素集合に分割するアルゴリズム|まだ使用しているのみで, 具体的な構造はわかっていない|
