def ReverseRotate(l: list) -> list:
    """180°回転させる"""
    h, w = len(l), len(l[0])
    ans = [[None] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            ans[h - i - 1][w - j - 1] = l[i][j]

    return ans

sample = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
print(*ReverseRotate(sample), sep="\n")