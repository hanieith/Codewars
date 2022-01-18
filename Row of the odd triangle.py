def odd_row(n):
    x = (n * (n-1)) + 1
    result = list()
    for i in range(x, (x+(n-1)*2)+1 , 2):
        result.append(i)
    return result