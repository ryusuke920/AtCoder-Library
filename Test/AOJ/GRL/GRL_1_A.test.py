# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A

import sys
sys.path.append("../../../")

from Graph import Dijkstra


def main():
    V, E, r = map(int, input().split())
    g = [[] for _ in range(V)]
    INF = 10**18
    for _ in range(E):
        s, t, d = map(int, input().split())
        g[s].append((t, d))

    dist = Dijkstra.dijkstra(r, g)
    for i in range(V):
        print(dist[i]) if dist[i] != INF else print("INF")


if __name__ == "__main__":
    main()