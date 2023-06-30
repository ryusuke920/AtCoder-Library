# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_D

import sys
sys.path.append("../../../")

from Tree import BinaryIndexedTree
import copy


def main():
    n = int(input())
    a = list(map(int, input().split()))

    x = copy.copy(a)
    print(BinaryIndexedTree.BIT(x))


if __name__ == "__main__":
    main()