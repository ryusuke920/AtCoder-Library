class Kruskal:
    def __init__(self, n: int, g: list) -> None:
        self.n = n
        self.g = g.sort(key=lambda x: x[2])
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


    def size(self, a: int) -> int:
        return -self.p[self.leader(a)]


    def cost(self, g: list) -> list:
        tree = []
        for u, v, cost in g:
            if self.same(u, v):
                continue
            self.merge(u, v)
            tree.append(cost)

        return tree


def main() -> None:
    n, m = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(m)]

    kruskal = Kruskal(n, g)
    print(sum(kruskal.tree(g)))


if __name__ == "__main__":
    main()