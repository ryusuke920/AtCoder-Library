# verification-helper: PROBLEM https://yukicoder.me/problems/no/713

import sys
sys.path.append("../../")

from Math import SieveOfEratosthenes


def main() -> None:
    print(sum(SieveOfEratosthenes.primes(int(input()))))


if __name__ == "__main__":
    main()