# verification-helper: PROBLEM https://yukicoder.me/problems/no/2570

import sys
sys.path.append("../../")

from Math import Divisor

def main() -> None:
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    p = set()
    for i in range(N):
        for j in Divisor.divisors(A[i]):
            p.add(j)

    ans = []
    for x in p:
        cnt = 0
        for i in range(N):
            cnt += min(A[i] % x, x - (A[i] % x))
        if cnt <= K:
            ans.append(x)

    print(max(ans))


if __name__ == "__main__":
    main()