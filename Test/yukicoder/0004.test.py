# verification-helper: PROBLEM https://yukicoder.me/problems/no/4

def main() -> None:

    n = int(input())
    w = list(map(int, input().split()))

    if sum(w) % 2:
        print('impossible')
    else:
        t = 10 ** 4 + 10
        dp = [[False] * t for _ in range(n + 1)]
        # dp[i][j] := i番目までの重りでjを作れるかどうか
        dp[0][0] = True
        for i in range(n):
            for j in range(t):
                if j - w[i] >= 0:
                    dp[i + 1][j] |= dp[i][j - w[i]]
                dp[i + 1][j] |= dp[i][j]
        
        print('possible') if dp[-1][sum(w) // 2] else print('impossible')


if __name__ == "__main__":
    main()