# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind

import sys
sys.path.append('../..')

from Tree import UnionFindTree

n, q = map(int, input().split())

uf = UnionFindTree.UnionFind(n)

for _ in range(q):
    t, u, v = map(int,input().split())
    if t == 0:
        uf.merge(u, v)
    elif t == 1:
        print(1) if uf.same(u, v) else print(0)