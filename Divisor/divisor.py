def divisor(x):
    num = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            num.append(i)
            if i != x // i:
                num.append(x // i)
    num.sort()
    return num

n = int(input())
div = divisor(n)
print(div)