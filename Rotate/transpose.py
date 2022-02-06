def TransposeRotate(l: list) -> list:
    """転置行列を求める"""
    ans = [[None] * h for _ in range(w)]
    for i in range(w):
        for j in range(h):
            ans[i][j] = l[j][i]

    return ans

h, w = map(int, input().split())
sample = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]] # 4 * 3
print(*TransposeRotate(sample), sep="\n")