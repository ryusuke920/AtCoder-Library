# verification-helper: PROBLEM https://yukicoder.me/problems/no/2559

def main() -> None:
    N, X = map(int, input().split())
    A, B = [0] * N, [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    
    ans = []
    for j in range(1, X + 1):
        cnt = 0
        for i in range(N):
            cnt = max(cnt, max(B[i] - abs(j - A[i]), 0))
        ans.append(cnt)

    print(*ans)


if __name__ == "__main__":
    main()