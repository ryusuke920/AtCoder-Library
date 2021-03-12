# 計算量は O (NlogN)
from bisect import bisect_left

def LIS(A, N): # 配列・長さ
    INF = 10 ** 18
    dp = [INF] * n
    for i in A:
        x = bisect_left(dp, i)
        dp[x] = i
    return(bisect_left(dp, INF))

n = 5
a = [5, 1, 3, 2, 4]
ans = LIS(a, n)
print(ans)