def combination(n, k):
    nCk = under = top = 1

    for i in range(2, k + 1):
        under *= i

    for i in range(k):
        top *= (n - i)


    nCk = top // under

    return nCk 

def factorization(n):
    arr = []
    tmp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            arr.append([i, cnt])
    if tmp != 1:
        arr.append([tmp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr
print(combination(136,14) // 2 ** 6 // 9)
