# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_3_D

import sys
sys.path.append("../../")

from MathLibrary import Divisor

def main() -> None:
    a, b, c = map(int, input().split())

    ans = 0
    for i in Divisor.divisors(c):
        if a <= i <= b:
            ans += 1
    
    print(ans)


if __name__ == "__main__":
    main()