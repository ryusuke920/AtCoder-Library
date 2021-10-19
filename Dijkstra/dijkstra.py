from heapq import heappush, heappop
import sys # 入力高速化
input = sys.stdin.readline

def dijkstra(s, graph): # (始点, グラフのリスト)
    INF = 10 ** 18
    dist = [INF] * n # INF で初期化
    check = [False] * n # Bool
    dist[s] = 0
    q = [(0, s)] # （距離・ノード）
    while q:
        v = heappop(q)[1] # 今いるノード
        if check[v]: continue # すでに行っていたらcontinue
        check[v] = True # 訪問済み
        for i, j in graph[v]: # 先のノード・距離
            if check[i] != False: continue
            if dist[i] <= dist[v] + j: continue
            dist[i] = dist[v] + j
            heappush(q, (dist[i], i)) # 必ず[0]が距離になるように（優先度付きキュー）
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