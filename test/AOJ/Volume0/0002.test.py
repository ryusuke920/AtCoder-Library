# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0002

def main():
    while True:
        try:
            a, b = map(int, input().split())
            print(len(str(a + b)))
        except:
            break
    
if __name__ == "__main__":
    main()