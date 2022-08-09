# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_C

import sys
sys.path.append("../../../")

from MathLibrary import PrimaryCheck

def main() -> None:
    ans = 0

    n = int(input())
    for _ in range(n):
        ans += int(PrimaryCheck.PrimaryCheck(int(input())))
    
    print(ans)


if __name__ == "__main__":
    main()