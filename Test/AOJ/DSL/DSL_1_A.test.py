# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A

import sys
sys.path.append("../../../")

from Tree import UnionFindTree

def main():
    n, q = map(int, input().split())

    uf = UnionFindTree.UnionFind(n)

    for _ in range(q):
        com, x, y = map(int, input().split())
        if com == 0:
            uf.merge(x, y)
        elif com == 1:
            print(int(uf.same(x, y)))


if __name__ == "__main__":
    main()
