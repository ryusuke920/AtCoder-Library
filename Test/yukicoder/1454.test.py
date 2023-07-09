# verification-helper: PROBLEM https://yukicoder.me/problems/no/1454

def main() -> None:
    n, m, x, y = map(int, input().split())
    a = list(map(int, input().split()))

    p = []
    for i in range(n):
        if a[i] <= y:
            continue
        p.append(a[i])
    
    n = len(p)
    if n <= m:
        print(sum(p))
    else:
        p.sort()
        for i in range(n - m):
            if p[i] >= x:
                exit(print("Handicapped"))
        p.sort(reverse=True)
        print(sum(p[:m]))


if __name__ == "__main__":
    main()