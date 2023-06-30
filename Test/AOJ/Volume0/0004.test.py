# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0004

def main():
    while True:
        try:
            a, b, c, d, e, f = map(int, input().split())
        except:
            break
            
        if a * e - b * d == 0:
            print("0.000 0.000")
        else:
            p, q = e * c - b * f, -d * c + a * f
            if p != 0:
                p /= (a * e - b * d)
            if q != 0:
                q /= (a * e - b * d)
            print("{:.3f}".format(p), "{:.3f}".format(q))


if __name__ == "__main__":
    main()