# 計算量：O(|V||E|)
def bellman_ford(s: int) -> list:
    '負のコストを持つ最短経路問題'
    INF = 10 ** 18
    dist = [INF] * n
    dist[s] = 0
    for i in range(n):
        update = False # 経路更新を行ったか
        for a, b, cost in g:
            if dist[a] > dist[b] + cost:
                dist[a] = dist[b] + cost
                update = True

        # 更新が行われなければそれが最短経路となる
        if not update:
            break

        if i == n - 1:
            return -1

    return dist

n, m = map(int, input().split())
g = []
for _ in range(m):
    u, v, cost = map(int, input().split())
    u -= 1
    v -= 1
    g.append((u, v, cost))
    g.append((v, u, cost))

ans = bellman_ford(0)

if ans == -1:
    print('Yes')
else:
    print(ans)