from bisect import bisect_left

def LIS(n: int, a: list) -> int:
    INF = 10 ** 18
    dp = [INF] * n
    for i in a:
        x = bisect_left(dp, i)
        dp[x] = i

    return bisect_left(dp, INF)

n = int(input())
a = list(map(int, input().split()))

cnt = LIS(n, a)
print(cnt)