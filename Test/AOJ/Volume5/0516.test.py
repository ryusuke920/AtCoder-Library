# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0516

import sys
sys.path.append("../../../")

from Math import MaxCumulativeSum

def main():
    while True:
        n, k = map(int, input().split())
        if (n, k) == (0, 0):
            exit()
        a = [int(input()) for _ in range(n)]
        ans = MaxCumulativeSum.MaxCumulativeSum(a, k)

        print(max(ans))


if __name__ == "__main__":
    main()