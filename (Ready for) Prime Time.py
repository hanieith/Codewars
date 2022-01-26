from math import sqrt
def is_simple(n: int) -> bool:
    if n % 2 == 0 and n != 2:
        return False
    for i in range (3, int(sqrt(n)) + 2, 2):
        if n % i == 0 and n != i:
            return False
    return True
def prime(n):
    result = []
    for i in range(2, n+1):
        if is_simple(i):
            result.append(i)
    return result