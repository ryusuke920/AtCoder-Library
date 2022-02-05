from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def dijkstra(s: int, graph: list):
    INF = 10 ** 18
    dist = [INF] * n
    check = [False] * n
    dist[s] = 0
    q = [(0, s)]
    while q:
        v = heappop(q)[1]
        if check[v]: continue
        check[v] = True
        for i, j in graph[v]:
            if check[i] != False: continue
            if dist[i] <= dist[v] + j: continue
            dist[i] = dist[v] + j
            heappush(q, (dist[i], i))
    return dist

n, m = map(int,input().split())
# n = int(input())
g = [[] for _ in range(n)]
for _ in range(m):
    x, y, cost = map(int,input().split())
    x -= 1
    y -= 1
    g[x].append((cost, y))
    g[y].append((cost, x))

d = dijkstra(0, g)