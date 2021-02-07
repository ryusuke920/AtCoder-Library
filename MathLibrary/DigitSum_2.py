# 桁の和を求める（strに変更して計算するパターン）
def DigitSum(num):
    num = str(num)
    digit_sum = 0
    for i in range(len(num)):
        digit_sum += int(num[i])
    return digit_sum

n = 1234567890
ans = DigitSum(n)
print(ans)