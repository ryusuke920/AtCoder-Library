def combination(n, k):
    nCk = 1
    mod = 10 ** 9 + 7

    for i in range(n - k + 1, n + 1):
        nCk *= i
        nCk %= mod

    for i in range(1, k + 1):
        nCk *= pow(i, mod - 2, mod)
        nCk %= mod
    return nCk

n = combination(400, 14)
print(n)