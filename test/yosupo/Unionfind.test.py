# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind

import sys
from pathlib import Path
sys.path.append(Path(__file__).parents[2].__str__())

from Tree import UnionFindTree

def main():
    n, q = map(int, input().split())

    uf = UnionFindTree.UnionFind(n)

    for _ in range(q):
        t, u, v = map(int,input().split())
        if t == 0:
            uf.merge(u, v)
        elif t == 1:
            print(int(uf.same(u, v)))

if __name__ == "__main__":
    main()
