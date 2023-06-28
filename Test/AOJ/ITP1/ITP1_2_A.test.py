# verification-helper: PROBLEM  https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_2_A&lang=ja


def main() -> None:
    a, b = map(int, input().split())
    if a < b:
        print("a < b")
    elif a > b:
        print("a > b")
    else:
        print("a == b")


if __name__ == "__main__":
    main()