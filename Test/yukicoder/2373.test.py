# verification-helper: PROBLEM https://yukicoder.me/problems/no/2373

def main() -> None:
    n = int(input())
    s = list(input())
    dp = [[False] * 4 for _ in range(n + 1)]
    # 0 := w, 1 := a, 2 := o, 3 := n
    if s[0] == "w":
        dp[1][0] = True
    if s[0] == "n":
        dp[1][3] = True
    if s[0] == "?":
        dp[1][0] = True
        dp[1][3] = True
    
    for i in range(2, n + 1):
        if dp[i - 1][0]:
            if s[i - 1] == "a" or s[i - 1] == "?":
                dp[i][1] = True
            if s[i - 1] == "o" or s[i - 1] == "?":
                dp[i][2] = True
        if dp[i - 1][1]:
            if s[i - 1] == "w" or s[i - 1] == "?":
                dp[i][0] = True
            if s[i - 1] == "n" or s[i - 1] == "?":
                dp[i][3] = True
        if dp[i - 1][2]:
            if s[i - 1] == "w" or s[i - 1] == "?":
                dp[i][0] = True
            if s[i - 1] == "n" or s[i - 1] == "?":
                dp[i][3] = True
        if dp[i - 1][3]:
            if s[i - 1] == "w" or s[i - 1] == "?":
                dp[i][0] = True
            if s[i - 1] == "n" or s[i - 1] == "?":
                dp[i][3] = True

    print("Yes") if dp[n][1] or dp[n][2] or dp[n][3] else print("No")


if __name__ == "__main__":
    main()