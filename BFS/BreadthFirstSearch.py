from collections import deque
h, w = map(int,input().split())
sy, sx = map(int,input().split())
gy, gx = map(int,input().split())
(sy, sx, gy, gx) = (sy - 1, sx - 1, gy - 1, gx - 1) # 0indexで設定する
grid = [[] for _ in range(h)] # h * w のgridマスを用意する

for i in range(h):
    C = list(input())
    for j in range(w):
        grid[i] = C

dist = [[10000] * w for _ in range(h)] # 各マスの最小距離を記録する２次元配列
for i in range(h):
    for j in range(w):
        if grid[i][j] == "#": # gridマスが # になっている場合は通れないので便宜上 -1 とする
            dist[i][j] = -1
dist[sy][sx] = 0 # スタート地点は０距離で行ける

q = deque()
q.append([sy, sx]) # (スタートのy座標, スタートのx座標)
d = [[1, 0], [-1, 0], [0, 1], [0, -1]] # ４方向への変化量

while q:
    v = q.popleft() # (今いるy座標, 今いるx座標)
    for i, j in d: # 変化量を足していく（配列の長さである4回分）
        if not (0 <= v[0] + i <= h - 1 and 0 <= v[1] + j <= w - 1): continue # 変化量を足した際に配列外になる場合は調べない
        if grid[v[0] + i][v[1] + j] == "#": continue # マスが通れない場合は当然調べない
        if dist[v[0] + i][v[1] + j] != 10000: continue # 10000でなければ既に調べたか行けない場所なので調べない
        dist[v[0] + i][v[1] + j] = dist[v[0]][v[1]] + 1
        q.append([v[0] + i, v[1] + j]) # 次に行く場所をdequeに追加する

print(dist[gy][gx])