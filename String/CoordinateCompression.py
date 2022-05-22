def CC(A: list) -> list:
    "座標圧縮"
    B = {j: i + 1 for i, j in enumerate(sorted(set(A)))}
    return B

x = [2, 5, 1, 21, 312, 23, 21]
ans = CC(x)
print(ans)