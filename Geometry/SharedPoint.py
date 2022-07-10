def SharedPoint(x1: int, y1: int, r1: int, x2: int, y2: int, r2: int) -> int:
    """2つの円の共有点の個数を求める"""
    # (x1, y1) を中心とした半径 r1 の円
    # (x - x1) ** 2 + (y - y1) ** 2 = r1 ** 2
    d = (x1 - x2) ** 2 + (y1 - y2) ** 2
    
    # r1 > r2
    if r1 < r2:
        r1, r2 = r2, r1
    
    if d == (r1 + r2) ** 2 or d == (r1 - r2) ** 2:
        return 1
    elif (r1 - r2) ** 2 < d < (r1 + r2) ** 2:
        return 2
    else:
        return 0

'''
類題
ABC259-D - Circumferences: https://atcoder.jp/contests/abc259/tasks/abc259_d
ACコード: https://atcoder.jp/contests/abc259/submissions/33150317
'''
