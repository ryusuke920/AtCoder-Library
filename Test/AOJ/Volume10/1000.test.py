# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1000&lang=en


def main():
    while True:
        try:
            a, b = map(int, input().split())
            print(a + b)
        except:
            break


if __name__ == "__main__":
    main()