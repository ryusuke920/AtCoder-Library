# 計算量：O(|V||E|)
def bellman_ford(n: int, g: list, s: int) -> list:
    INF = float('inf')
    dist = [INF] * n
    dist[s] = 0

    for i in range(n):
        update = False # 経路更新を行ったか
        for a, b, cost in g:
            if dist[b] > dist[a] + cost:
                dist[b] = dist[a] + cost
                update = True

        # 更新が行われなければそれが最短経路となる
        if not update:
            break

        if i == n - 1:
            return -1

    return dist


def main() -> None:
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


if __name__ == "__main__":
    main()