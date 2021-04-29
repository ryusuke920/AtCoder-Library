"""
計算量はO(1)
"""

def XorToN(N: int) -> int:
    if N % 4 == 0:
        return N
    elif N % 4 == 1:
        return 1
    elif N % 4 == 2:
        return N + 1
    elif N % 4 == 3:
        return 0

x = XorToN(196)
print(x)
