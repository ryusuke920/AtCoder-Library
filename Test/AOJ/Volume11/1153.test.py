# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1153&lang=jp

def main() -> None:
    while True:
        n, m = map(int, input().split())
        if (n, m) == (0, 0):
            exit()
        
        s = [int(input()) for _ in range(n)]
        t = [int(input()) for _ in range(m)]

        sum1, sum2 = sum(s), sum(t)
        num = 10**18
        ans = [0, 0]
        for i in range(n):
            for j in range(m):
                if sum1 - s[i] + t[j] == sum2 - t[j] + s[i]:
                    if s[i] + t[j] < num:
                        ans = [s[i], t[j]]
                        num = s[i] + t[j]
        
        print(*ans) if num != 10**18 else print(-1)


if __name__ == "__main__":
    main()