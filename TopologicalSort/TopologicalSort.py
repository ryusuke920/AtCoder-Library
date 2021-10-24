from collections import defaultdict
from heapq import heappop, heappush

n, m = map(int,input().split())

g = [[] for _ in range(n)]
d = defaultdict(int) # d[i] := 頂点iに入ってくる辺の個数

for _ in range(m):
    a, b = map(int,input().split())
    g[a - 1].append(b - 1)
    d[b - 1] += 1

q = []
# スタート地点を決める
for i in range(n):
    if d[i] == 0:
        heappush(q, i)

ans = []
l = 0 # 答えの長さ
while l < n:
    if len(q) == 0:
        exit(print(-1))

    v = heappop(q)
    ans.append(v + 1)
    l += 1
    for i in g[v]:
        d[i] -= 1
        if d[i] == 0:
            heappush(q, i)

print(*ans)