def ReverseRotate(l: list, h: int, w: int) -> list:
    """180°回転させる"""
    ans = [[None] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            ans[h - i - 1][w - j - 1] = l[i][j]

    return ans

sample = [[0, 1, 2, 3], [5, 6, 7, 8], [9, 10, 11, 12]] # 3 * 4
print(*ReverseRotate(sample ,3, 4), sep="\n")