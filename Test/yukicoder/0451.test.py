# verification-helper: PROBLEM https://yukicoder.me/problems/no/451

def main() -> None:
    n = int(input())
    b = [int(input()) for _ in range(n)]
    i, mid = 0, 0
    a = [1] * (n + 1)
    while i < n:
        if i % 2:
            a[i + 1] = a[i] - b[i]
        else:
            a[i + 1] = b[i] - a[i]
        
        if a[i + 1] <= 0 or a[i + 1] > 10**18:
            a[0] += 1 - a[i + 1]
            i = -1
            mid += 1
        if mid == 10:
            exit(print(-1))
        i += 1
    
    if a[0] <= 0:
        exit(print(-1))
    
    print(n + 1)
    for i in range(n + 1):
        print(a[i])


if __name__ == "__main__":
    main()