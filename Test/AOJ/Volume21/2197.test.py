# verification-helper: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2197&lang=jp

def main():
    while True:
        n = int(input())
        if n == 0:
            exit()
        
        ans = 0
        for start in range(1, n + 1):
            num = start
            i = start + 1
            while num < n:
                num += i
                if num == n:
                    ans += 1
                    break
                i += 1
        
        print(ans)


if __name__ == "__main__":
    main()