# verification-helper: PROBLEM https://judge.yosupo.jp/problem/associative_array

from collections import defaultdict

def main() -> None:
    d = defaultdict(int)

    Q = int(input())
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 0:
            k, v = query[1], query[2]
            d[k] = v
        elif query[0] == 1:
            k = query[1]
            print(d[k])

if __name__ == "__main__":
    main()