# verification-helper: PROBLEM https://yukicoder.me/problems/no/1808

def is_ok(k: int) -> bool:
    check = True
    cnt = 0
    for i in range(n):
        cnt += a[i]
        if cnt >= k * (i + 1): continue
        check = False

    return check


def binary_search(left: int, right: int) -> int:
    while right - left > 1:
        mid = (left + right) // 2
        if is_ok(mid):
            left = mid
        else:
            right = mid

    return left


def main():
    global n, a

    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    print(binary_search(-1, 10**18) // m)


if __name__ == "__main__":
    main()