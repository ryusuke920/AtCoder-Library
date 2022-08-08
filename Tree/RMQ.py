# このセグ木はPythonだとTLEするのでPyPyを推奨します

"""
〜segfuncの使い方について〜
update(k, x): k番目の要素をxに更新する
query(l, r): [l, r)（l <= k < r の区間）から値kを取得する
"""

def segfunc(x: int, y: int) -> int:
    "ここで求めたい処理を行う, max(x, y) や x ^ y など"
    return min(x, y)


class SegTree:
    def __init__(self, segfunc, init_val, ide_ele):
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.n = len(init_val)
        self.num = 2 ** self.n.bit_length()
        self.seg = [self.ide_ele] * 2 * self.num
        for i in range(self.n):
            self.seg[i + self.num - 1] = init_val[i]
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
        return res

if __name__ == "__main__":
    n, q = map(int,input().split()) # 配列の長さ・クエリ数
    a = list(map(int,input().split())) # 配列
    seg = SegTree(segfunc, a, float('inf')) # オブジェクトの作成