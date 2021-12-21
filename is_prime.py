def is_simple(n: int) -> bool:
    if n % 2 == 0 and n != 2:
        return False
    for i in range (3, int(sqrt(n)) + 2, 2):
        if n % i == 0 and n != i:
            return False
    return True