def Mod_Combination(n, k, mod):
    p, q = 1, 1
    for i in range(n-k+1, n+1):
        p = (p * i) % mod
    for i in range(2, k+1):
        q = (q * i) % mod
    return int(p * Mod_Inverse(q, mod) % mod)

def Ext_Gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = Ext_Gcd(b, a % b)
        x -= (a // b) * y
        return d, y, x

def Mod_Inverse(a, mod):
    return Ext_Gcd(a, mod)[1] % mod

for i in range(10 ** 5):
    Mod_Combination(10 ** 5, 10 ** 5 // 2, 10**9 + 7)