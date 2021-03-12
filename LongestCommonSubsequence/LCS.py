def LCS(A, B): # １つ目の配列・２つ目の配列
    # dp[i][j] := Aのi番目, Bのj番目までで作れる最大共通部分文字列
    dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                dp[i + 1][j + 1] = max(dp[i][j] + 1, dp[i + 1][j], dp[i][j + 1])
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    return(dp[len(A)][len(B)])

a = input().rstrip()
b = input().rstrip()
ans = LCS(a, b)
print(ans)