# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_10_C&lang=ja

from statistics import stdev

def main():
    while True:
        n = int(input())
        if n == 0:
            exit()
        print(stdev(list(map(int, input().split()))))


if __name__ == "__main__":
    main()