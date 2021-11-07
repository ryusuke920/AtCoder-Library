import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
g = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

for i in range(n):
    g[i].sort()

ans = [] # 頂点集合
depth = [] # 深さの集合
def dfs(now: int, prev: int, cnt: int):
    ans.append(now + 1)
    depth.append(cnt)
    for nxt in g[now]:
        if nxt == prev: continue
        dfs(nxt, now, cnt + 1)
        ans.append(now + 1)
        depth.append(cnt)

dfs(0, -1, 0)
print(*ans)
print(*depth)