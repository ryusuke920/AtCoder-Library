# verification-helper: PROBLEM https://yukicoder.me/problems/no/167

import sys
sys.set_int_max_str_digits(10**9)

def main() -> None:

    n = int(input())
    m = int(input())

    print(pow(n, m, 10))


if __name__ == "__main__":
    main()