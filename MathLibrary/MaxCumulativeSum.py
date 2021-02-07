# 配列の累積和の部分和の最大値を求める
def MaxCumulativeSum(num_array, k): # 配列・区間幅
    max_cumulative_sum = [] # 区間幅分の部分和を格納する配列
    count = 0
    for i in range(k):
       count += num_array[i]
    max_cumulative_sum.append([count, 0, 0 + k]) # 部分和・左端・右端
    
    for i in range(len(num_array) - k):
        count += num_array[i + k]
        count -= num_array[i]
        max_cumulative_sum.append([count, i + 1, i + 1 + k])
    
    max_cumulative_sum.sort(key = lambda x: x[0], reverse = True) # 降順にソート
    return max_cumulative_sum[0]


a = [1, 4, -1, 9, 34, 21, -12, 31]
ans = MaxCumulativeSum(a, 3) # 配列・区間幅
print(ans)