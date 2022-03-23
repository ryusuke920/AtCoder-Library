# 木の中心を求める O(N^3)

from collections import deque

def bfs(s: int) -> list:
    "幅優先探索を行い、頂点 s からの距離を求める"
    dist = [10000] * N
    dist[s] = 0
    q = deque([s])
    while q:
        v = q.popleft()
        for nxt in g[v]:
            if dist[nxt] == 10000:
                dist[nxt] = dist[v] + 1
                q.append(nxt)
    
    return dist

N = int(input())

# 隣接行列の作成
g = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

# 頂点 1 からの距離を求める
dist = bfs(0)

# 最も遠い頂点からもう一度幅優先探索を行う
max_dist = max(dist)
for i in range(N):
    if dist[i] == max_dist:
        # 木の直径を求める
        diameter = max(bfs(i))
        break

# ある頂点が木の中心であるならば、すべての頂点への距離は「(木の直径 / 2)以下」となる
center = []
for i in range(N):
    dist = bfs(i)
    check = True
    for j in range(N):
        if dist[j] > (diameter + 1) // 2:
            check = False
    if check:
        center.append(i + 1)

# 木の中心をソートして出力する
center.sort()
for i in center:
    print(i)