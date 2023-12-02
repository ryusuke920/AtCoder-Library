# verification-helper: PROBLEM https://yukicoder.me/problems/no/2558

def main() -> None:
    A, B, a, b = map(int, input().split())
    for x in range(A * B + 1):
        if x % A == a and x % B == b:
            print(x)
            exit()


if __name__ == "__main__":
    main()