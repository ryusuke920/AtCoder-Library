# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1608&lang=jp

def main():
    while True:
        n = int(input())
        if n == 0:
            exit()
        a = list(map(int, input().split()))
        a.sort()

        ans = 10**18
        for i in range(n - 1):
            ans = min(ans, a[i + 1] - a[i])

        print(ans)


if __name__ == "__main__":
    main()