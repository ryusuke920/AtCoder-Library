# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_B

import sys
sys.path.append("../../../")

from math import gcd

def main():
    x, y = map(int, input().split())
    print(gcd(x, y))


if __name__ == "__main__":
    main()