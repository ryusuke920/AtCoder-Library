# verification-helper: PROBLEM https://yukicoder.me/problems/no/9

from heapq import heapify, heappop, heappush

def main() -> None:

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = []
    for start in range(n):
        q = []
        heapify(q)
        for i in range(n):
            heappush(q, (a[i], 0))
        
        for i in range(n):
            p, num = heappop(q)
            p += b[(start + i) % n] // 2
            heappush(q, (p, num + 1))

        ma = 0
        for i in range(n):
            ma = max(ma, heappop(q)[1])
        
        ans.append(ma)

    print(min(ans))


if __name__ == "__main__":
    main()