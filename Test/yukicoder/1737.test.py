# verification-helper: PROBLEM https://yukicoder.me/problems/no/1737

import sys
sys.path.append("../../")

from Math import Factorization

def main() -> None:
    n = int(input())

    if n == 1:
        exit(print(0))

    ans = 0
    for i, j in Factorization.factorization(n):
        ans += i * j

    print(ans)


if __name__ == "__main__":
    main()