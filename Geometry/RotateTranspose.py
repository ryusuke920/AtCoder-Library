def TransposeRotate(l: list) -> list:
    """転置行列を求める"""
    h, w = len(l), len(l[0])
    ans = [[None] * h for _ in range(w)]
    for i in range(w):
        for j in range(h):
            ans[i][j] = l[j][i]

    return ans

sample = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
print(*TransposeRotate(sample), sep="\n")