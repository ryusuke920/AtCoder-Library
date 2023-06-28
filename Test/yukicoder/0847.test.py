# verification-helper: PROBLEM https://yukicoder.me/problems/no/847

import sys
sys.path.append("../../")

from Math import factorization

def dfs(a: list, now: int):
    
    global ans

    if len(a) == l and now <= m:
        ans += 1
        return

    for i in range(fac[len(a)][1] + 1):

        now *= fac[len(a)][0] ** i

        if now <= m:
            dfs(a + [i], now)
            now //= fac[len(a)][0] ** i
        else:
            return

n, k, m = map(int, input().split())

fac = factorization.factorization(n)
l = len(fac)

for i in range(l):
    fac[i][1] *= k

ans = 0
dfs([], 1)
print(ans)