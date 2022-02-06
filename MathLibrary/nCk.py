def calc_facinv(n: int) -> list:
    '逆元テーブルを作成する'

    # 階乗テーブルの作成
    fac = [0] * (n + 1)
    fac[0] = 1
    for i in range(1, n + 1):
        fac[i] = fac[i - 1] * i
        fac[i] %= mod
    
    # 逆元テーブルの作成
    fac_inv = [0] * (n + 1)
    fac_inv[0] = 1
    for i in range(1, n + 1):
        fac_inv[i] = pow(fac[i], mod - 2, mod)
    
    return fac, fac_inv

def combination(n: int, k: int) -> int:
    '''nCkを計算する'''

    return fac[n] * fac_inv[k] * fac_inv[n - k] % mod

n, k = map(int, input().split())

mod = 10 ** 9 + 7
fac, fac_inv = calc_facinv(n)

ans = combination(n, k)
print(ans)