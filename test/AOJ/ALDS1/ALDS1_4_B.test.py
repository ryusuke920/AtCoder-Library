# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B

import sys
sys.path.append("../../../")

def main():
    n = int(input())
    s = set(list(map(int, input().split())))
    q = int(input())
    t = set(list(map(int, input().split())))
    
    print(len(s & t))


if __name__ == "__main__":
    main()
