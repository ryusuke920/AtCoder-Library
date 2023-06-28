# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1172&lang=jp

import sys
sys.path.append("../../../")

from Math import SieveOfEratosthenes
from bisect import bisect_left

def main() -> None:

    primes_list = SieveOfEratosthenes.primes(123456*2 + 100)

    while True:
        n = int(input())
        if n == 0:
            exit()
        
        if n == 1:
            print(1)
        else:
            p, q = bisect_left(primes_list, n + 1), bisect_left(primes_list, 2 * n)
            print(q - p)


if __name__ == "__main__":
    main()