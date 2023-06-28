# verification-helper: PROBLEM https://judge.yosupo.jp/problem/many_aplusb

def main() -> None:

    T = int(input())

    for _ in range(T):
        A, B = map(int, input().split())
        print(A + B)


if __name__ == "__main__":
    main()