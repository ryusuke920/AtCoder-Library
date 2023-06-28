# 10進数 -> 2進数への変換
def DeciamlToBinary(num):
    binary_number = ""
    while num > 0:
        binary_number += str(num % 2)
        num //= 2
    return int(binary_number[::-1])

n = 1234567890
ans = DeciamlToBinary(n)
print(ans)