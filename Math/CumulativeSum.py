# 配列の累積和を求める
def CumulativeSum(num_array):
    for i in range(len(num_array) - 1):
        num_array[i + 1] += num_array[i]
    return num_array


a = [1, 4, -1, 9, 34, 21, -12, 31]
ans = CumulativeSum(a)
print(ans)