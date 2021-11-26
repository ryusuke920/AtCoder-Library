def PrimaryCheck(x):
    if n == 1: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())
num = PrimaryCheck(n)
print(num)