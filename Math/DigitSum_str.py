def DigitSum(num: str) -> int:
    '''str 型の桁和を求める'''
    return sum([int(num[i]) for i in range(len(num))])

print(DigitSum('1234567890'))