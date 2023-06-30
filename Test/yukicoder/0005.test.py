# verification-helper: PROBLEM https://yukicoder.me/problems/no/5

def main() -> None:

    l = int(input())
    n = int(input())
    w = sorted(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        ans += w[i]
        if ans > l:
            exit(print(i))
    print(n)


if __name__ == "__main__":
    main()