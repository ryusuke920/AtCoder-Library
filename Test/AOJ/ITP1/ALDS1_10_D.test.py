# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_10_D&lang=ja
# verification-helper: ERROR 1e-5

def main():
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    ans = [0] * 4
    for i in range(n):
        ans[0] += abs(x[i] - y[i])
        ans[1] += abs(x[i] - y[i]) ** 2
        ans[2] += abs(x[i] - y[i]) ** 3
        ans[3] = max(ans[3], abs(x[i] - y[i]))
    
    print(ans[0])
    print(ans[1]**0.5)
    print(ans[2]**(1/3))
    print(ans[3])


if __name__ == "__main__":
    main()