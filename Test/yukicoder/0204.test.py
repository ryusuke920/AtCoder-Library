# verification-helper: PROBLEM https://yukicoder.me/problems/no/204


def main() -> None:
    d = int(input())
    c1 = input()
    c2 = input()
    s = "x" * 14 + c1 + c2 + "x" * 14
    ans = 0
    for i in range(27):
        if i + d > 42:
            continue
        p = [i for i in s]
        cnt = 0
        for j in range(d):
            if p[i + j] == "x":
                cnt += 1    
                p[i + j] = "o"
        if cnt <= d:
            num = 0
            for i in range(42):
                if p[i] == "o":
                    num += 1
                else:
                    ans = max(ans, num)
                    num = 0
            ans = max(ans, num)
    
    print(ans)


if __name__ == "__main__":
    main()