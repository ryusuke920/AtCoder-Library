# verification-helper: PROBLEM https://yukicoder.me/problems/no/64

def main() -> None:
    f0, f1, n = map(int, input().split())
    a = [f0, f1, f0 ^ f1]
    print(a[n % 3])


if __name__ == "__main__":
    main()