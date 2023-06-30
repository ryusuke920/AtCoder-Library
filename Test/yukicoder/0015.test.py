# verification-helper: PROBLEM https://yukicoder.me/problems/no/9

from itertools import product
from bisect import bisect_right

def main() -> None:

    n, s = map(int, input().split())
    p = [int(input()) for _ in range(n)]

    cnt = min(20, n)
    item1 = []
    bisect_item1 = []
    for i in product([0, 1], repeat=cnt):
        money, item = 0, []
        for j in range(cnt):
            if i[j] == 1:
                money += p[j]
                item.append(j + 1)
        item1.append([money, item])
        bisect_item1.append(money)

    cnt = max(0, n - 20)
    item2 = []
    bisect_item2 = []
    for i in product([0, 1], repeat=cnt):
        money, item = 0, []
        for j in range(cnt):
            if i[j] == 1:
                money += p[j + 20]
                item.append(j + 21)
        item2.append([money, item])
        bisect_item2.append(money)

    item2.sort(key=lambda x: x[0])
    bisect_item2.sort()

    ans = []
    for money, item in item1:
        if money > s: continue
        p = bisect_right(bisect_item2, s - money)
        if money + bisect_item2[p - 1] == s:
            a = item
            b = item2[p - 1][1]
            ans.append(sorted(a + b))

    ans.sort()
    for i in ans:
        print(*i)


if __name__ == "__main__":
    main()