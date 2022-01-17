def sum_fibs(n):
    sum = 0
    a = 0
    b = 1
    for i in range(2,n+1):
        a , b = b, a+b
        if b % 2 == 0:
            sum += b
    return sum