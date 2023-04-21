# verification-helper: PROBLEM https://yukicoder.me/problems/no/697

import sys
sys.path.append("../../")

from collections import deque

h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

# dist[i][j] := INF -> 池でまだ見てない, -1 -> 地面で通れない
dist = [[-1] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if a[i][j]:
            dist[i][j] = 0

cnt = 1 # 今見ている池の番号
q = deque()
for i in range(h):
    for j in range(w):
        if a[i][j]:
            q.append((i, j))
            dist[i][j] = cnt
            break
    break

d = ((1, 0), (-1, 0), (0, 1), (0, -1))
for i in range(h):
    for j in range(w):
        if not (dist[i][j] == 0 or dist[i][j] == cnt): continue
        if dist[i][j] == 0:
            q.append((i, j))
        while q:
            vy, vx = q.popleft()
            dist[vy][vx] = cnt
            for dy, dx in d:
                y = vy + dy
                x = vx + dx
                if not (0 <= x < w and 0 <= y < h): continue
                if dist[y][x] != 0: continue
                dist[y][x] = dist[vy][vx]
                q.append((y, x))
        cnt += 1

ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans, dist[i][j])

print(ans)