# verification-helper: PROBLEM https://yukicoder.me/problems/no/1

from collections import defaultdict

n = int(input())
c = int(input())
v = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
y = list(map(int, input().split()))
m = list(map(int, input().split()))

INF = 10 ** 18
d_time = defaultdict(list) # d_time[i_j] := iからjへかかる時間
d_cost = defaultdict(list) # d_cost[i_j] := iからjへかかるコスト

for i in range(v):
    d_time[f'{s[i]}_{t[i]}'].append(m[i])
    d_cost[f'{s[i]}_{t[i]}'].append(y[i])
#print(d_time)
#print(d_cost)
# dp[i][j] := i番目の町にいて、かかったコストがjである時のかかった時間の最小値
# dp[i][j] = min(dp[i][j], dp[k][j - y[j]] + c[j]) (1 <= k < i)

dp = [[INF] * (c + 1) for _ in range(n + 1)]
for j in range(c + 1):
    dp[1][j] = 0

for i in range(1, n + 1):
    for k in range(1, i):
        for j in range(c + 1):
            for p, q in zip(d_cost[f'{k}_{i}'], d_time[f'{k}_{i}']):
                if j - p >= 0:
                    # k -> iに行く場合の更新路があるか考える。 (k < i)
                    dp[i][j] = min(dp[i][j], dp[k][j - p] + q)

ans = INF
for j in range(c + 1):
    ans = min(ans, dp[-1][j])

print(ans) if ans != INF else print(-1)