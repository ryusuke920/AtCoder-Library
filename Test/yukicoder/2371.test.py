# verification-helper: PROBLEM https://yukicoder.me/problems/no/2371

def main() -> None:
    h, m = map(int, input().split())
    time = h * 60 + m

    if time <= 7 * 60 + 29:
        print("Yes")
    elif time <= 8 * 60 + 29:
        print("Late")
    else:
        print("No")


if __name__ == "__main__":
    main()