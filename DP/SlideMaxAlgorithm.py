# むずい
from collections import deque

def SlideMinAlgorithm(a: list, k: int) -> list:
    n = len(a)
    ans = [-1] * (n - k + 1)
    q = deque()
    q.append((a[0], 0))
    for i in range(1, k):
        if q[0][0] < a[i]:
            q.appendleft((a[i], i))
    ans[0] = q[0][0]

    for i in range(1, n - k + 1):
        if q[0][1] < i:
            q.popleft()
        while q:
            if q[-1][0] >= a[i + k - 1]:
                q.pop()
            else:
                break
        q.append((a[i + k - 1], i + k - 1))
        ans[i] = q[0][0]

    return ans


def main() -> None:
    a = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(SlideMinAlgorithm(a, 4))


if __name__ == "__main__":
    main()