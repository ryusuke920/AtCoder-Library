# verification-helper: PROBLEM https://yukicoder.me/problems/no/208

def main() -> None:
    x, y = map(int, input().split())
    x2, y2 = map(int, input().split())

    if x == y and x2 == y2 and x2 < x:
        print(max(x, y) + 1)
    else:
        print(max(x, y))


if __name__ == "__main__":
    main()