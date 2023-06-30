# verification-helper: PROBLEM https://yukicoder.me/problems/no/8

def main() -> None:
    p = int(input())
    for _ in range(p):
        n, k = map(int, input().split())
        if n <= k:
            print("Win")
        elif (n - 1) % (k + 1) == 0:
            print("Lose")
        else:
            print("Win")


if __name__ == "__main__":
    main()