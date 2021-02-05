from itrtools import product

def BitSearch(x, l): # リスト・数
    num = 0
    for i in product([0, 1], repeat = l):
        for j in range(l):
            if i[j] == 1: # 1 <-> bitが立っている時
                # O(1)