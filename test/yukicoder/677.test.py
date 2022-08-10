# verification-helper: PROBLEM https://yukicoder.me/problems/no/677

n = int(input())

ans = []
for i in range(n + 1):
    for j in range(n + 1):
        ans.append(2 ** i * 5 ** j)

print(*sorted(ans), sep='\n')