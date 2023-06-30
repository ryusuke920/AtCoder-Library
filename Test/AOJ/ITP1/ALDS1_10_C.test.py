# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_10_C&lang=ja
# verification-helper: ERROR 1e-4

from statistics import pstdev

def main():
    while True:
        n = int(input())
        if n == 0:
            exit()
        print(pstdev(list(map(int, input().split()))))


if __name__ == "__main__":
    main()