# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2944&lang=jp

def main() -> None:
    while True:
        n, m = map(int, input().split())
        if (n, m) == (0, 0):
            exit()
        a = list(map(int, input().split()))

        ans = 0
        for i in range(n):
            ans += min(m // n, a[i])

        print(ans)


if __name__ == "__main__":
    main()