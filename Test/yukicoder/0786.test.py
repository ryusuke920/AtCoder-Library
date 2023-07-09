# verification-helper: PROBLEM https://yukicoder.me/problems/no/786

def main() -> None:
    n = int(input())
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    print(dp[n])


if __name__ == "__main__":
    main()