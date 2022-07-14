# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind

from Tree.UnionFindTree import UnionFind

def main():
    n, q = map(int, input().split())

    uf = UnionFind(n)

    for _ in range(q):
        t, u, v = map(int,input().split())
        print(1) if uf.same(u, v) else print(0) if t else uf.merge(u, v)

if __name__ == "__main__":
    main()