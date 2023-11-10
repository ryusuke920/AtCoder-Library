def factorization(n: int) -> int:
    arr, tmp = [], n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            arr.append([i, cnt])

    if tmp != 1:
        arr.append([tmp, 1])

    return arr


def main() -> None:
    print(factorization(2592))


if __name__ == "__main__":
    main()