# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_12_A&lang=ja
# 最小全域木（プリム法）
from heapq import heappop, heappush, heapify

n = int(input())

g = []
for _ in range(n):
    l = list(map(int,input().split()))
    g.append([(cost, i) for i, cost in enumerate(l) if cost != -1])

visited = [0] * n
connection = 0
q = []
q.append((0, 0))
heapify(q)

ans = 0
while q:
    cost, v = heappop(q)
    if visited[v]: continue

    visited[v] = 1
    connection += 1
    ans += cost

    for nxt in g[v]:
        heappush(q, nxt)
    
    if connection == n:
        break

print(ans)