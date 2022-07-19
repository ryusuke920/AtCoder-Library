# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0001


def main():
    print(*sorted([int(input()) for _ in range(10)], reverse=True)[:3], sep='\n')


if __name__ == "__main__":
    main()
