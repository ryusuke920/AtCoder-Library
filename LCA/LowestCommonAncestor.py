"""
〜segfuncの使い方について〜
update(k, x): k番目の要素をxに更新する
query(l, r): [l, r)（l <= k < r の区間）から値kを取得する
"""
def segfunc(x: int, y: int) -> int:
    "ここで求めたい処理を行う, max(x, y) や x ^ y など"
    return min(x, y)

"""
〜単位元の一覧について〜
最小値：float("inf")
最大値：-float("inf")
XOR：0
区間和：0
区間積：1
最大公約数：0
"""

class SegTree:
    def __init__(self, segfunc, init_val, ide_ele, euler):
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.euler = euler
        self.num = 2 ** n.bit_length()
        self.seg = [self.ide_ele] * 2 * self.num
        for i in range(n):
            self.seg[i+self.num - 1] = init_val[i]
        for i in range(self.num - 2, -1, -1):
            self.seg[i] = self.segfunc(self.seg[2 * i + 1], self.seg[2 * i + 2])

    def update(self, k, x):
        k += self.num - 1
        self.seg[k] = self.segfunc(self.seg[k], x)
        while k:
            k = (k - 1) // 2
            self.seg[k] = self.segfunc(self.seg[k * 2 + 1], self.seg[k * 2 + 2])

    def query(self, l, r):
        " l は0index, r は1index"
        if r <= l:
            return self.ide_ele
        l += self.num - 1
        r += self.num - 2
        res = self.ide_ele
        while r - l > 1:
            if l & 1 == 0:
                res = self.segfunc(res, self.seg[l])
            if r & 1 == 1:
                res = self.segfunc(res, self.seg[r])
                r -= 1
            l = l // 2
            r = (r - 1) // 2
        if l == r:
            res = self.segfunc(res, self.seg[l])
        else:
            res = self.segfunc(res, self.segfunc(self.seg[l], self.seg[r]))
        return res,l, r,self.seg

def EulerTour(g):
    ans = [] # 頂点集合
    depth = [] # 深さの集合
    def dfs(now: int, prev: int, cnt: int):
        ans.append(now)
        depth.append(cnt)
        for nxt in g[now]:
            if nxt == prev: continue
            dfs(nxt, now, cnt + 1)
            ans.append(now)
            depth.append(cnt)
    
    dfs(0, -1, 0)

    return ans, depth

n = int(input())
g = [[] for _ in range(n)]
for i in range(n):
    a = list(map(int,input().split()))[1:]
    for j in a:
        g[i].append(j)
        g[j].append(i)

for i in range(n):
    g[i].sort()

euler, depth = EulerTour(g) # 頂点集合・深さの集合

fast = [-1] * n # 最初に出現した位置

for i, j in enumerate(euler):
    if fast[j] == -1:
        fast[j] = i

print( euler, "頂点の集合")
print(depth,"深さ")
print("最初に出てきた位置", fast)

INF = 10 ** 18
ide_ele = INF # 初期値（単位元）の設定
n = len(euler)
seg = SegTree(segfunc, depth, ide_ele, euler) # オブジェクトの作成

q = int(input())
for i in range(q):
    u, v = map(int,input().split())
    x, y = fast[u], fast[v]
    if x > y:
        x, y = y, x
    ans = seg.query(x, y + 1)
    print(ans)