# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.p = [-1] * n


    def leader(self, a):
        while self.p[a] >= 0:
            a = self.p[a]
        return a


    def merge(self, a, b):
        x = self.leader(a)
        y = self.leader(b)

        if x == y:
            return x

        if self.p[x] > self.p[y]:
            x, y = y, x

        self.p[x] += self.p[y]
        self.p[y] = x

        return x

    def same(self, a, b):
        return self.leader(a) == self.leader(b)

    def size(self, a):
        return -self.p[self.leader(a)]

n, q = map(int,input().split())

uf = UnionFind(n)

for _ in range(q):
    t, u, v = map(int,input().split())
    if t == 0:
        uf.merge(u, v)
    elif t == 1:
        print(1) if uf.same(u, v) else print(0)