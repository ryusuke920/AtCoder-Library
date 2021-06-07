def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    return

def binary_search(left, right):
    while abs(left - right) > 1:
        mid = (left + right) // 2
        if is_ok(mid):
            right = mid
        else:
            left = mid

INF = 10 ** 18
l, r = -1, INF
print(binary_search(l, r))