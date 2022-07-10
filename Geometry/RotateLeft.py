def LeftRotate(l: list) -> list:
    """左に90°回転させる"""
    h, w = len(l), len(l[0])
    ans = [[None] * h for _ in range(w)]
    for i in range(h):
        for j in range(w):
            ans[w - j - 1][i] = l[i][j]

    return ans

sample = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
print(*LeftRotate(sample), sep="\n")