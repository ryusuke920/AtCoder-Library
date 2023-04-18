# verification-helper: PROBLEM https://yukicoder.me/problems/no/182

from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)
for i in range(n):
    d[a[i]] += 1

ans = 0
for i in d.values():
    ans += i == 1

print(ans)