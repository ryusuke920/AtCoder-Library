# 木の中心を求める O(N^3)
# 1-indexedで表された木の中心となりうる頂点の集合を改行区切りで出力します。
from collections import deque
from collections import defaultdict

def bfs(s: int) -> tuple:
    "幅優先探索を行い、頂点 s からの距離を求める"
    dist = [10000] * N
    dist[s] = 0
    q = deque([s])

    vertexmemo = defaultdict(list)
    vertexmemo[0].append(s)
    while q:
        v = q.popleft()
        for nxt in g[v]:
            if dist[nxt] == 10000:
                dist[nxt] = dist[v] + 1
                vertexmemo[dist[nxt]].append(nxt)
                q.append(nxt)
    
    return dist, vertexmemo

N = int(input())

g = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

dist, vmap = bfs(0)
Dlist, LPM = bfs(vmap[max(dist)][0])
Diameter = max(Dlist)

FromA = bfs(LPM[0][0])[1]
FromB = bfs(LPM[Diameter][0])[1]
pre_center = FromA[Diameter//2] if Diameter%2 == 0 else FromA[Diameter//2]+FromA[(Diameter+1)//2]
center = list()

for i in FromB[Diameter//2] if Diameter%2 == 0 else FromB[Diameter//2]+FromB[(Diameter+1)//2]:
    if i in pre_center:
        center.append(i+1)

for i in sorted(center):
    print(i)