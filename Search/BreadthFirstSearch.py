from collections import deque

def bfs(sy: int, sx: int) -> list:
    '始点座標を受け取ってBFS'
    INF = 10 ** 18
    dist = [[INF] * w for _ in range(h)]
    dist[sy][sx] = 0
    
    # 障害物の確認
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#':
                dist[i][j] = -1
    
    # BFS
    d = ((0, 1), (0, -1), (1, 0), (-1, 0))
    q = deque()
    q.append((sy, sx))

    while q:
        vy, vx = q.popleft()
        for dy, dx in d:
            y = vy + dy
            x = vx + dx
            if not (0 <= x < w and 0 <= y < h): continue
            if grid[y][x] == '#': continue
            if dist[y][x] != INF: continue
            dist[y][x] = dist[vy][vx] + 1
            q.append((y, x))
    
    return dist

h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]

dist = bfs(0, 0)
print(*dist, sep='\n')