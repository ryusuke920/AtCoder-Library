import sys
debug = lambda *x : print(*x, file = sys.stderr)
"""
これを使用すると、標準エラー出力になるので、printしてもジャッジに反映されない
"""

a = [1, 2, 3, 4, 5]
word = "ryusuke"
debug(a, word)

# ABC199のAを解いてみる
A, B, C = map(int,input().split())
if A ** 2 + B ** 2 < C ** 2:
    print("Yes")
else:
    print("No")