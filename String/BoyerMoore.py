from collections import defaultdict

def BoyerMoore(s: str, t: str) -> bool:
    '''文字列 s の中に t が存在するかを判別する'''
    skip_table = defaultdict(lambda : -1)
    for i, j in enumerate(t[::-1]):
        if skip_table[j] == -1:
            skip_table[j] = i
    
    l_s = len(s)
    l_t = len(t)

    if l_s < l_t:
        return False
    else:
        i = l_t - 1
        cnt = 0
        while i < l_s:
            if s[i] == t[-1 - cnt]:
                cnt += 1
                i -= 1
            else:
                i += l_t if skip_table[s[i]] == -1 else skip_table[s[i]]
                cnt = 0

            if cnt == l_t:
                print(f'[{i + 1}, {i + l_t}] の区間に {t} が見つかりました。')
                return True
        
        return False

s = 'abcdefghijklmnopqrstuvwxyz'
t = 'def'
print(BoyerMoore(s, t))