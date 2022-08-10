# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_13_A

from itertools import permutations

k = int(input())
rc = [list(map(int, input().split())) for _ in range(k)]

for p in permutations(range(8)):
    flag = True
    for i, j in rc:
        if p[i] != j:
            flag = False

    if not flag:
        continue

    for k in range(8):
        for l in range(8):
            if k == l:
                continue
            if abs(p[k] - p[l]) == abs(k - l):
                flag = False

    if flag:
        for i in p:
            ans = ["."] * 8
            ans[i] = "Q"
            print("".join(ans))