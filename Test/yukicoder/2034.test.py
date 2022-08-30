# verification-helper: PROBLEM https://yukicoder.me/problems/no/2034

from collections import defaultdict

n = int(input())
s = input()

d = defaultdict(int)
rev_d = defaultdict(int)
for i, j in enumerate("abcdefghijklmnopqrstuvwxyz"):
    d[j] = i
    rev_d[i] = j

ans = []
for i in s:
    ans.append(rev_d[26 - d[i] - 1])

print(*ans, sep='')