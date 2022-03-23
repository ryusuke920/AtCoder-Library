# 木の直径を求める O(N^3)

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

g = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)


dist = bfs(0)

max_dist = max(dist)
for i in range(N):
    if dist[i] == max_dist:
        diameter = max(bfs(i))
        break

print(diameter)