def is_ok(arg):
    if 1:
        return True
    else:
       return False

def binary_search(left: int, right: int) -> int:
    while abs(left - right) > 1:
        mid = (left + right) // 2
        if is_ok(mid):
            left = mid
        else:
            right = mid

    return left

INF = 10 ** 18
l, r = -1, INF
print(binary_search(l, r))