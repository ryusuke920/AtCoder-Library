# verification-helper: PROBLEM https://yukicoder.me/problems/no/2093

def main() -> None:
    N, I = map(int, input().split())
    s, a = [0] * N, [0] * N
    for i in range(N):
        s[i], a[i] = map(int, input().split())
    
    dp = [[0] * (I + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(I + 1):
            if 0 <= j - s[i - 1] <= I:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - s[i - 1]] + a[i - 1])
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
    
    print(dp[N][I])


if __name__ == "__main__":
    main()