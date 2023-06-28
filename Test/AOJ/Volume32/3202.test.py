# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=3202&lang=jp

from collections import deque

def main() -> None:
    while True:
        w, h, n, d, b = map(int, input().split())
        if (w, h, n, d, b) == (0, 0, 0, 0, 0):
            exit()
        
        grid = [[0] * w for _ in range(h)]

        x, y = [0] * n, [0] * n
        for i in range(n):
            x[i], y[i] = map(lambda x: int(x) - 1, input().split())
            grid[y[i]][x[i]] = -1
        
        ans = 1
        q = deque()
        q.append((y[b - 1], x[b - 1]))
        grid[y[b - 1]][x[b - 1]] = 1
        while q:
            vy, vx = q.popleft()
            for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                for k in range(1, d + 1):
                    ny = vy + dy * k
                    nx = vx + dx * k
                    if not (0 <= ny < h and 0 <= nx < w):
                        continue
                    if grid[ny][nx] == -1:
                        ans += 1
                        grid[ny][nx] = 1
                        q.append((ny, nx))
                    if grid[ny][nx] == 0:
                        grid[ny][nx] = 1
        
        print(ans)


if __name__ == "__main__":
    main()