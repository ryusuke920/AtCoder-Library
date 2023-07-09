# verification-helper: PROBLEM https://yukicoder.me/problems/no/44


def main() -> None:

    n = int(input())

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    

    print(dp[n])


if __name__ == "__main__":
    main()