# verification-helper: PROBLEM https://yukicoder.me/problems/no/1737

import sys
sys.path.append("../../")

from MathLibrary import Factorization

n = int(input())

if n == 1:
    print(0)
    exit()

ans = 0
for i, j in Factorization.factorization(n):
    ans += i * j

print(ans)