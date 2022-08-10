# verification-helper: PROBLEM https://judge.yosupo.jp/problem/associative_array

from collections import defaultdict
import sys
input = sys.stdin.readline

def main() -> None:
    d = defaultdict(int)

    Q = int(input())
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 0:
            d[query[1]] = query[2]
        elif query[0] == 1:
            print(d[query[1]])

if __name__ == "__main__":
    main()