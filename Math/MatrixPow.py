def matrix_multi(a: list, b: list, mod=998244353) -> list:
    len_a, len_b, len_b_zero = len(a), len(b), len(b[0])
    c = [[0] * len(b[0]) for _ in range(len_a)]
    for i in range(len_a):
        for j in range(len_b_zero):
            for k in range(len_b):
                c[i][j] += a[i][k] * b[k][j]
                c[i][j] %= mod

    return c


def matrix_pow(a: list, n: int) -> list:
    len_a = len(a)
    cnt = [[0] * len_a for _ in range(len_a)]

    for i in range(len_a):
        cnt[i][i] = 1

    while n > 0:
        if n & 1:
            cnt = matrix_multi(a, cnt)

        a = matrix_multi(a, a)
        n >>= 1

    return cnt


def main() -> None:
    n = int(input())

    fibonacci = [[1, 1], [1, 0]]
    fibonacci = matrix_pow(fibonacci, n)

    ans = fibonacci[1][0]
    # print(*fibonacci, sep="\n")
    print(ans)


if __name__ == "__main__":
    main()