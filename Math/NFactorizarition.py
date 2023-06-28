# 2msの場合は10^6まで行ける
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

def nCkFactorization(k: int) -> list:
    """1,2, ... ,n を全て素因数分解する"""

    divisors = [[] for _ in range(k + 1)]
    a = [i for i in range(k + 1)]
    num = primes_list(k)

    for p in num:
        for i in range(p, k + 1, p):
            while a[i] % p == 0:
                divisors[i].append(p)
                a[i] //= p

    return divisors

num = nCkFactorization(100)
#print(*num, sep="\n")
for i in range(len(num)):
    print(i, num[i])