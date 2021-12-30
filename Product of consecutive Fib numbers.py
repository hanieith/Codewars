def(prod):
    a = 0
    b = 1
    while (a * b) < prod:
        a, b = b, a + b
    return a * b == prod