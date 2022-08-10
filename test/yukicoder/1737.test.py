# verification-helper: PROBLEM https://yukicoder.me/problems/no/1737

import sys
sys.path.append("../../")

from MathLibrary import Factorization

n = int(input())

if n == 1:
    exit(print(0))

fac = Factorization.factorization(n)

ans = 0
for i, j in fac:
    ans += i * j

print(ans)