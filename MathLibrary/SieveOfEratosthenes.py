def primes(n: int) -> list:
    "素数の列挙を行う"

    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False

    return [i for i in range(n + 1) if is_prime[i]]

x = primes(100) # 素数の全列挙
print(len(x), x)