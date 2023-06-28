# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1640&lang=jp

def main():
    while True:
        n = int(input())
        if n == 0:
            exit()
        d = list(map(int, input().split()))

        ans = 0
        for i in range(n - 3):
            if d[i : i + 4] == [2, 0, 2, 0]:
                ans += 1
        
        print(ans)


if __name__ == "__main__":
    main()