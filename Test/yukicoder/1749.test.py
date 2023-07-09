# verification-helper: PROBLEM https://yukicoder.me/problems/no/1749

def main() -> None:
    n, m, t = map(int, input().split())
    
    g = [[] for _ in range(n)]
    for _ in range(m):
        x, y = map(int, input().split())
        g[x].append(y)
        g[y].append(x)
    mod = 998244353

    # dp[i][j] := i 日目に都市 j で感染している人数の合計
    dp = [[0] * (n + 1) for _ in range(t + 1)]
    dp[0][0] = 1
    for i in range(1, t + 1):
        for j in range(n):
            cnt = 0
            for nxt in g[j]:
                cnt += dp[i - 1][nxt]
                cnt %= mod

            dp[i][j] = cnt
            dp[i][j] %= mod

    print(dp[t][0])


if __name__ == "__main__":
    main()