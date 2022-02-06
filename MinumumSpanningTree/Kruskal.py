# クラスカル法
# 出典：https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_f

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
    if x == y: return x
    if self.p[x] > self.p[y]:
      x, y = y, x
    self.p[x] += self.p[y]
    self.p[y] = x
    return x

  def same(self, a, b): return self.leader(a) == self.leader(b)

  def size(self, a): return -self.p[self.leader(a)]

n, m = map(int, input().split())

uf = UnionFind(n)

# (a, b, cost)の無向グラフ

g = [list(map(int, input().split())) for _ in range(m)]
g.sort(key=lambda x: x[2])

ans = 0
for i, j, cost in g:
    if uf.same(i, j): continue
    uf.merge(i, j)
    ans += cost

print(ans)