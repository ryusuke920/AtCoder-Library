def divisors(n):
    divisor = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor.append(i)
            if i != n // i:
                divisor.append(n // i)

    divisor.sort()
    return divisor

x = divisors(120)
print(x)