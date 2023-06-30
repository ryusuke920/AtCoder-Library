# verification-helper: PROBLEM https://yukicoder.me/problems/no/3

from collections import deque

def main() -> None:

    n = int(input())

    dist = [0] * (n + 1)
    dist[1] = 1

    q = deque([1])
    while q:
        v = q.popleft()
        cnt = 0
        for i in range(60):
            if v >> i & 1:
                cnt += 1

        a = v - cnt
        if 1 <= a <= n:
            if dist[a] == 0:
                dist[a] = dist[v] + 1
                q.append(a)

        b = v + cnt
        if 1 <= b <= n:
            if dist[b] == 0:
                dist[b] = dist[v] + 1
                q.append(b)

    print(dist[-1]) if dist[-1] != 0 else print(-1)


if __name__ == "__main__":
    main()