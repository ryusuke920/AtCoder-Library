import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
g = [[] for _ in range(n)]
for i in range(n):
    a = list(map(int, input().split()))[1:]
    for j in a:
        g[i].append(j)
        g[j].append(i)

LogN = 1
while 1 << LogN < n: 
    LogN += 1

depth = [0] * n
root = [[0] * n for _ in range(LogN)]

def dfs(now: int, prev: int):
    root[0][now] = prev
    for nxt in g[now]:
        if nxt == prev: continue
        depth[nxt] = depth[now] + 1
        dfs(nxt, now)
dfs(0, -1)

for i in range(LogN - 1):
    for j in range(n):
        root[i + 1][j] = root[i][root[i][j]]

def LCA(u, v):
    # depth[u] < depth[v]
    if depth[u] > depth[v]:
        u, v = v, u

    dist = depth[v] - depth[u]
    for i in range(LogN):
        if dist >> i & 1:
            v = root[i][v]

    if u == v:
        return u

    for i in reversed(range(LogN)):
        if root[i][u] != root[i][v]:
            u = root[i][u]
            v = root[i][v]
    return root[0][u]

q = int(input())
for _ in range(q):
    u, v = map(int, input().split())
    print(LCA(u, v))