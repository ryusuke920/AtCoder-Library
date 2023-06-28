# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1147&lang=jp

def main() -> None:
    while True:
        n = int(input())
        if n == 0:
            exit()
        
        a = [int(input()) for _ in range(n)]
        print((sum(a) - (min(a) + max(a))) // (n - 2))


if __name__ == "__main__":
    main()