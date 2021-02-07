# 桁の和を求める（intのまま計算するパターン）
def DigitSum(num):
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10
    return digit_sum

n = 1234567890
ans = DigitSum(n)
print(ans)