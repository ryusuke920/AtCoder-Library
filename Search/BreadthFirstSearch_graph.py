from collections import deque

def bfs(n: int, g:list, s: int) -> list:
    n = len(g)
    INF = float('inf')
    dist = [INF] * n
    dist[s] = 0
    
    q = deque()
    q.append(s)

    while q:
        prev = q.popleft()
        for nxt in g[prev]:
            if dist[nxt] != INF: continue
            dist[nxt] = dist[prev] + 1
            q.append(nxt)
    
    return dist

def main() -> None:
    n = int(input())

    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    
    bfs(0, g)



if __name__ == "__main__":
    main()