# ２進数 -> 10進数への変換
def BinaryToDecimal(num):
    num = str(num)[::-1]
    decimal_number = 0
    for i in range(len(num)):
        decimal_number += int(num[i]) * (2 ** i)
    return decimal_number

n = 1010010011111010001
ans = BinaryToDecimal(n)
print(ans)