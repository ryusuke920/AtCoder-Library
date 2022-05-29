def XorToN(N: int) -> int:
    "0 〜 N までの XOR の値を返す関数"
    
    if N % 4 == 0:
        return N
    
    if N % 4 == 1:
        return 1
    
    if N % 4 == 2:
        return N + 1
    
    if N % 4 == 3:
        return 0

print(XorToN(196))