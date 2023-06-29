def MaxCumulativeSum(num_array: list, k: int):
    max_cumulative_sum = []
    count = 0
    for i in range(k):
       count += num_array[i]
    max_cumulative_sum.append([count, 0, 0 + k])
 
    for i in range(len(num_array) - k):
        count += num_array[i + k]
        count -= num_array[i]
        max_cumulative_sum.append([count, i + 1, i + 1 + k])
    
    max_cumulative_sum.sort(key = lambda x: x[0], reverse=True)
    return max_cumulative_sum[0]


def main() -> None:
    a = [1, 4, -1, 9, 34, 21, -12, 31]
    ans = MaxCumulativeSum(a, 3) # 配列・区間幅
    print(ans)


if __name__ == "__main__":
    main()