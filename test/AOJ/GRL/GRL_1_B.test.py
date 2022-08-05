# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B

import sys
from pathlib import Path

p = Path(__file__).parts
sys.path.append('/'.join(p[:p.index('AtCoder-Library') + 1]))

from Graph import BellmanFord
from Search import BreadthFirstSearch_graph

def main():
    V, E, r = map(int, input().split())
    s, t, d = [0] * E, [0] * E, [0] * E

    g = [[] for _ in range(V)]
    for i in range(E):
        s[i], t[i], d[i] = map(int, input().split())
        g[s[i]].append(t[i])

    dist = BreadthFirstSearch_graph.bfs(V, g, r)
    judge = [False] * V

    for i in range(V):
        if dist[i] != float('inf'):
            judge[i] = True
    
    g = []
    for i in range(E):
        if judge[s[i]]:
            g.append((s[i], t[i], d[i]))

    ans = BellmanFord.bellman_ford(V, g, r)
    if ans == -1:
        print('NEGATIVE CYCLE')
    else:
        for i in range(V):
            if ans[i] == float('inf'):
                print('INF')
            else:
                print(ans[i])


if __name__ == "__main__":
    main()
