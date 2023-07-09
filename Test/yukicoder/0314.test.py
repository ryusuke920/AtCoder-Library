# verification-helper: PROBLEM https://yukicoder.me/problems/no/314

def main() -> None:
    n = int(input())
    
    dp = [[0] * 3 for _ in range(n + 1)]
    dp[1][1] = 1
    mod = 10**9 + 7

    for i in range(2, n + 1):
        dp[i][0] = dp[i - 1][1] + dp[i - 1][2]
        dp[i][1] = dp[i - 1][0]
        dp[i][2] = dp[i - 1][1]
        for j in range(3):
            dp[i][j] %= mod
    
    print(sum(dp[n]) % mod)

if __name__ == "__main__":
    main()