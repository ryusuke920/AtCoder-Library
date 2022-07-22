# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind

from Tree.UnionFindTree import UnionFind

def main():
    n, q = map(int, input().split())

    uf = UnionFind(n)

    for _ in range(q):
        t, u, v = map(int, input().split())
        if t == 0:
            uf.merge(u, v)
        elif t == 1:
            print(int(uf.same(u, v)))

if __name__ == "__main__":
    main()
