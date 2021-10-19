def LeftRotate(l: list, h: int, w: int) -> list:
    """左に90°回転させる"""
    ans = [[None] * h for _ in range(w)]
    for i in range(h):
        for j in range(w):
            ans[j][i] = l[i][j]

    return ans

sample = [[0, 1, 2, 3], [5, 6, 7, 8], [9, 10, 11, 12]] # 3 * 4
print(*LeftRotate(sample ,3, 4), sep="\n")