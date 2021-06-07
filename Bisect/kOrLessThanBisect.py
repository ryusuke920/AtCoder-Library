from bisect import bisect_left, bisect_right

def OrLessThan(K: int, A: list) -> int:
    "配列Aの中のうち、k以下の個数と終わりの0indexを返すライブラリ"
    "-1の時は解が無い時"
    return bisect_right(A, K), (-1 if bisect_right(A, K) == 0 else bisect_right(A, K) - 1)

a = [10, 10, 10, 11, 11, 12, 12, 12, 12, 14, 16, 12, 18, 10, 12]
a.sort()
print(a)
num, ind = OrLessThan(12, a) # 個数, 始まりの0index
print(num, ind)