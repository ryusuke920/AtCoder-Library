# verification-helper: PROBLEM https://yukicoder.me/problems/no/2

import sys
sys.path.append("../../")

from MathLibrary import factorization

def main() -> None:
    n = int(input())
    a = factorization.factorization(n)

    or_ = 0
    for i in range(len(a)):
        or_ ^= a[i][1]

    print("Alice") if or_ != 0 else print("Bob")


if __name__ == "__main__":
    main()