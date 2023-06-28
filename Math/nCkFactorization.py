def primes_list(n):
    """エラトステネスの篩でn以下の素数を全列挙する"""
    if n == 0:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if not is_prime[i]: continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

def nCkFactorization(n: int, k: int) -> list:
    """nCkの 1,2,...,k, n,n-1,...,n-k+1を全て素因数分解する"""

    # 分子
    divisors_1 = [[] for _ in range(k)]
    a = [n - i for i in range(k)]
    num = primes_list(int(n ** 0.5) + 1)

    for p in num:
        for i in reversed(range(n - k + 1 + p - (n - k + 1) % p if (n - k + 1) % p != 0 else n - k + 1, n + 1, p)):
            while a[n - i] % p == 0:
                divisors_1[n - i].append(p)
                a[n - i] //= p

    for i in range(len(a)):
        if a[i] != 1:
            divisors_1[i].append(a[i])

    # 分母
    divisors_2 = [[] for _ in range(k + 1)]
    a = [i for i in range(k + 1)]
    num = primes_list(k) # 素数の全列挙
    
    for p in num:
        for i in range(p, k + 1, p):
            while a[i] % p == 0:
                divisors_2[i].append(p)
                a[i] //= p
    
    return divisors_1, divisors_2

x, y = nCkFactorization(100, 30)
print("分子")
print(*x, sep="\n")
print("分母")
print(*y, sep="\n")