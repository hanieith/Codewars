def prev_mult_of_three(n):
    while n > 2:
        if n % 3 == 0:
            return n
        else:
            n = n // 10
    else:
        return None
