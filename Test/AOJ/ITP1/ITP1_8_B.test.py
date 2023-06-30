# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_11_A&lang=ja

import sys
sys.path.append("../../../")

from Math import DigitSum_int

def main() -> None:
    while True:
        n = int(input())
        if n == 0:
            exit()
        
        print(DigitSum_int.DigitSum(n))


if __name__ == "__main__":
    main()