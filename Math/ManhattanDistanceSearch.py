def manhattan_distance(li: list, k: int) -> int: # 返り値注意
    "マンハッタン距離で行ける場所を全探索する（tはマンハッタン距離の半径）"
    tmp = 0 # ここは例
    for i in range(k - 1, h - (k - 1)):
        for j in range(k - 1, w - (k - 1)):
            cnt = 0 # ここは例
            for t in range(2):
                if t == 0: # ((i,j)マスを含む k 個)
                    for l in reversed(range(k)):
                        for x in range(j - l, j + l + 1):
                            y = i - (k - (l + 1))
                            if li[y][x] == "1": cnt += 1 # ここは例
                elif t == 1: # ((i,j)マスを含まない k-1 個)
                    for l in reversed(range(k - 1)):
                        for x in range(j - l, j + l + 1):
                            y = i + (k - (l + 1))
                            if li[y][x] == "1": cnt += 1 # ここは例
            tmp = max(tmp, cnt) # ここは例
    return tmp # ここは例

"""
5 6 2
010111
100100
010010
100101
011010

上図の 5*6 のグリッドで k=2 の時の 1 の含まれる最大の個数を出力する
"""
h, w, k = map(int,input().split()) # 縦、横、マンハッタン距離の半径
grid = [list(input().rstrip()) for _ in range(h)]
ans = manhattan_distance(grid, k)
print(ans)