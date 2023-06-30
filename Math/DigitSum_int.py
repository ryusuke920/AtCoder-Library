def DigitSum(num: int) -> int:
    '''int 型の桁和を求める'''
    digit_sum = 0

    while num > 0:
        digit_sum += num % 10
        num //= 10

    return digit_sum