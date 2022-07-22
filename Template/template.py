import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
printd = lambda *x : print(*x, file = sys.stderr)

from math import ceil, floor, sin, cos, tan, acos, asin, atan, radians, factorial, exp, degrees
from collections import defaultdict, deque, Counter
from itertools import product, permutations, combinations, combinations_with_replacement
from heapq import heapify, heappop, heappush
from bisect import bisect, bisect_left, bisect_right


def min_int(a: int, b: int) -> int:
    "2数の最小値"
    return a if a <= b else b


def min_list(a: list) -> int:
    "リストの最小値"
    global INF
    cnt = INF
    for i in range(len(a)):
        if a[i] < cnt:
            cnt = a[i]

    return cnt


def min_list(a: list) -> int:
    "リストの最大値"
    global INF
    cnt = -INF
    for i in range(len(a)):
        if a[i] > cnt:
            cnt = a[i]

    return cnt


def max_int(a: int, b: int) -> int:
    "2数の最大値"
    return a if a >= b else b


def OutOfRange(h: int, w: int, vy: int, vx: int) -> bool:
    "BFSなどの配列外参照"
    d = ((1, 0), (-1, 0), (0, 1), (0, -1))
    for dy, dx in d:
        y = vy + dy
        x = vx + dx
        if not (0 <= x < w and 0 <= y < h):
            return False
        else:
            return True


def main() -> None:
    INF = 10 ** 18


if __name__ == '__main__':
    main()