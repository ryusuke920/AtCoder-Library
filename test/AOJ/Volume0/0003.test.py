# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0003

def main():
    N = int(input())
    for _ in range(N):
        a, b, c = sorted(list(map(int, input().split())))
        print("YES") if a ** 2 + b ** 2 == c ** 2 else print("NO")


if __name__ == "__main__":
    main()