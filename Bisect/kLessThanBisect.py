from bisect import bisect_left, bisect_right

def LessThan(K: int, A: list) -> int:
    "配列Aの中のうち、k未満の個数と終わりの0indexを返すライブラリ"
    "-1の時は解が無い時"
    return bisect_left(A, K), (-1 if bisect_left(A, K) == 0 else bisect_left(A, K) - 1)

a = [10, 10, 10, 11, 11, 12, 12, 12, 12, 14, 16, 12, 18, 10, 12]
a.sort()
print(a)
num, ind = LessThan(12, a) # 個数, 始まりの0index
print(num, ind)