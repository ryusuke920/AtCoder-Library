# verification-helper: PROBLEM https://judge.yosupo.jp/problem/staticrmq

import sys
input = sys.stdin.readline

sys.path.append("../../../")

from Tree import RMQ

def main():
    N, Q = map(int,input().split())
    a = list(map(int,input().split()))
    seg = RMQ.SegTree(RMQ.segfunc, a, float('inf'))

    for _ in range(Q):
        l, r = map(int, input().split())
        print(seg.query(l, r))

if __name__ == "__main__":
    main()