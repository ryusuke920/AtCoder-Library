# verification-helper: PROBLEM https://yukicoder.me/problems/no/1639

import sys
sys.path.append("../../")

from Graph import Kruskal

n = int(input())

g = []
for _ in range(n * (n - 1) // 2):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    g.append((a, b, c))

Kruskal = Kruskal.Kruskal(n, g)
ans = Kruskal.cost(g)

print(max(ans))