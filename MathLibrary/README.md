# AtCoder-Library

[![Actions Status](https://github.com/ryusuke920/AtCoder-Library/workflows/verify/badge.svg)](https://github.com/ryusuke920/AtCoder-Library/actions) [![ryusuke_h](https://img.shields.io/endpoint?url=https%3A%2F%2Fatcoder-badges.now.sh%2Fapi%2Fatcoder%2Fjson%2Fryusuke_h)](https://atcoder.jp/users/ryusuke_h)

[AtCoder](https://atcoder.jp/) のライブラリを保管しています。

(*stores AtCoder-Library.*)  

## MathLibrary
|File Name|Algorithm|Explanation|
|:--:|:--:|:--:|
|[BinaryToDecimal.py](BinaryToDecimal.py)|2進数 -> 10進数への変換|2進数を10進数に変換してくれる|
|DecimalToBinary.py|10進数 -> 2進数への変換|10進数を2進数に変換してくれる|
|[DigitSum_int.py](DigitSum_int.py)|桁和を求める|int の数字列の桁和を求める|
|[DigitSum_str.py](DigitSum_str.py)|桁和を求める|str の文字列の桁和を求める|
|divisor.py|約数列挙|約数の列挙を行ってくれる|
|ExtGCD.py|拡張ユークリッドの互除法|ap + bq = d := gcd(a, b)となる (p, q, d) を返す|
|FromFloatToInt.py|float -> int|floatの誤差計算を防ぐためにintに変換して計算する|
|factorization.py|素因数分解|素因数分解を行ってくれる|
|PrimaryCheck.py|素数判定|その数が素数かどうかの判定を行ってくれる  一般的には十分高速だが, 競プロ界隈だと遅い|
|[SieveOfEratosthenes.py](SieveOfEratosthenes.py)|エラトステネスの篩|素数を列挙を行う, 計算量は O(√Nlog√N)?|
|[XorToN.py](XorToN.py)|０〜NまでのXORをとる|計算量はO(1)|
|CumulativeSum.py|累積和|累積和を行ってくれる|
|MaxCumulativeSum.py|区間累積和の最大・最小問題|区間累積和の最大・最小を求められる|
|nCk.py|combinationの計算|nCkの計算を高速に行える, 計算量はO(K)|
|nCk_2.py|combinationの計算|nCk.pyのpowを最後に持ってきたから高速?, 計算量はO(K)|
