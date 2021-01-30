def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False # 便宜上false判定にしてる
    is_prime[1] = False # 便宜上false判定にしてる
    for i in range(2, n + 1):
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

n = 100
x = primes(n) # 素数の全列挙
l = len(x) # 素数の数
print(x)
print(l)