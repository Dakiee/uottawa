def sum_odd_divisors(n):
    newn = abs(n)
    if newn == 0:
        return None
    else:
        num = 0
    for i in range(1, newn + 1):
            if newn % i == 0 and i % 2 == 1:
                num += i
    return num
