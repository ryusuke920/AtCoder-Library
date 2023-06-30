# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0002

def main():
    while True:
        try:
            a, b = map(int, input().split())
        except:
            break
        
        print(len(str(a + b)))


if __name__ == "__main__":
    main()