def rle(S):
    tmp, cnt, ans = S[0], 1, ''
    for i in range(1, len(S)):
        if tmp == S[i]:
            cnt += 1
        else:
            ans += tmp + str(cnt)
            tmp = S[i]
            cnt = 1
    ans += tmp + str(cnt)
    return ans

s = "RRRLLRLRRLLLLRLRLRR"
print(rle(s))