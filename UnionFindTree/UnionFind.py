
def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def same(x,y):
    return find(x) == find(y)

def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    if x < y:
        x, y = y, x
    par[x] = y

n, m = map(int,input().split())
par = [i for i in range(n)]
for i in range(m):
    a, b = map(int,input().split())
    unite(a - 1, b - 1)

ans = [0] * n
for i in range(n):
    ans[find(i)] += 1
print(max(ans))