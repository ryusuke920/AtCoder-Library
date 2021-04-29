"""
２進数に直した際の i 桁目 (i >= 1) について
周期：p = 2 ** i
余り：r = n % 2 ** i
セット数：n // 2 ** i
１セットに含まれる１の個数：p * 2 ** (i - 1)
余り内の１の個数：r <= 2 ** (i - 1)だったら０, それ以外ならr - 2 ** (i - 1)
合計数 mod2 の値に 2 ** (i - 1)

計算量はO(logN)
"""

def XorToN(N: int) -> int:
    "０〜NまでのXORの値を返す関数"
    N += 1
    XorAns, i = 0, 1
    while True:
        if 2 ** (i - 1) > N:
            break
        p = N // (2 ** i) # 周期
        r = N % (2 ** i) # 余り
        num = (p * (2 ** (i - 1))) + max(0, r - 2 ** (i - 1))
        num %= 2 # XORを取る
        XorAns += num * 2 ** (i - 1)
        i += 1
    return XorAns

x = XorToN(196)
print(x)

"""
for i in range(100):
    print(F"i = {i}, i までのXORは{XorToN(i)}, ２進数に変換すると{bin(XorToN(i))[2:]}")
"""