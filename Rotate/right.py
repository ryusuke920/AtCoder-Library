def RightRotate(l: list, h: int, w: int) -> list:
    """右に90°回転させる"""
    ans = [[None] * h for _ in range(w)]
    for i in range(h):
        for j in range(w):
            ans[j][h - i - 1] = l[i][j]

    return ans

sample = [[0, 1, 2, 3], [5, 6, 7, 8], [9, 10, 11, 12]] # 3 * 4
print(*RightRotate(sample ,3, 4), sep="\n")