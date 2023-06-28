# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_11_B&lang=ja

import sys
sys.path.append("../../../")

from Math import Dice

def main() -> None:
    up, front, right, left, back, down = map(int, input().split())
    d = {}
    d[1] = up
    d[2] = front
    d[3] = right
    d[4] = left
    d[5] = back
    d[6] = down

    rev_d = {}
    rev_d[up] = 1
    rev_d[front] = 2
    rev_d[right] = 3
    rev_d[left] = 4
    rev_d[back] = 5
    rev_d[down] = 6

    q = int(input())
    for _ in range(q):
        up, front = map(int, input().split())
        dice = Dice.Dice(0, rev_d[up], 2, rev_d[front], 0, 0)
        print(d[dice.status()[4]])


if __name__ == "__main__":
    main()