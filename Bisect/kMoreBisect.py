from bisect import bisect_left, bisect_right

def More(K: int, A: list) -> int:
    "配列Aの中のうち、kより大きいものの個数と始まりの0indexを返すライブラリ"
    "-1の時は解が無い時"
    return len(A) - bisect_right(A, K), (bisect_right(A, K) if bisect_right(A, K) <= len(A) - 1 else -1)

a = [10, 10, 10, 11, 11, 12, 12, 12, 12, 14, 16, 12, 18, 10, 12]
a.sort()
print(a)
num, ind = More(12, a) # 個数, 始まりの0index
print(num, ind)