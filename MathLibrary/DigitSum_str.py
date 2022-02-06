def DigitSum(num: str) -> int:
    '''str 型の桁和を求める'''
    return sum([int(num[i]) for i in range(len(num))])

n = '1234567890'
print(DigitSum(n))