class UnionFind:
    def __init__(self, n: int) -> None:
        self.n = n
        self.p = [-1] * n


    def leader(self, a: int) -> int:
        while self.p[a] >= 0:
            a = self.p[a]
        return a


    def merge(self, a: int, b: int) -> int:
        x = self.leader(a)
        y = self.leader(b)

        if x == y:
            return x

        if self.p[x] > self.p[y]:
            x, y = y, x

        self.p[x] += self.p[y]
        self.p[y] = x

        return x

    def same(self, a: int, b: int) -> bool:
        return self.leader(a) == self.leader(b)

    def groups(self) -> list:
        member = [[] for _ in range(self.n)]
        for i in range(self.n):
            member[self.leader(i)].append(i)
        return member

    def size(self, a: int) -> int:
        return -self.p[self.leader(a)]


def main() -> None:
    N, M = map(int, input().split())

    UF = UnionFind(N)

    for _ in range(m):
        A, B = map(lambda x: int(x) - 1,input().split())
        UF.merge(A, B)

    ans = 0
    for i in range(N):
        ans = max(ans, UF.size(i))

    print(ans)


if __name__ == "__main__":
    main()