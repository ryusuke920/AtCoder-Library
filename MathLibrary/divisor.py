def divisor(x):
    divisor = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            divisor.append(i)
            if i != x // i:
                divisor.append(x // i)

    divisor.sort()
    return divisor

n = int(input())
num = divisor(n)
print(num)