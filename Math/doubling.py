class Doubling():
    def __init__(self, n, k_max, f) -> None:
        """要素数nのダブリングテーブルを作成します。"""

        k_bits = k_max.bit_length()

        # dub[i][j] = 値jを2**i回操作した結果
        dub = [[0] * n for _ in range(k_bits)]

        # 1回(2**0回)操作した結果を作成
        for j in range(n):
            dub[0][j] = f(j)

        # 2**i回操作した結果を順に作成
        # 2**(i-1)回操作を2回すれば2**i回操作したことになる
        for i in range(1, k_bits):
            for j in range(n):
                dub[i][j] = dub[i - 1][dub[i - 1][j]]

        self.doubling_table = dub

    def get(self, x, k):
        """xをk回操作した値を取得します。"""
        # kをビットごとに分解して、2**a + 2**b + 2**c + ... の形で考える。
        # xを2**a回操作した結果を2**b回操作した結果を2**c回操作… のように順に適用する
        now = x
        for i in range(k.bit_length()):
            if k>>i & 1:
                now = self.doubling_table[i][now]

        return now

def calc():
    "関数を定義する"
    return

n, k = map(int,input().split())
# nの最大値, k回, 関数
dub = Doubling(10 ** 5, k, calc)

# nをk回繰り返した先
print(dub.get(n, k))