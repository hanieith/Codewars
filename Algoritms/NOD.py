def nod(a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

#fast algoritm

def nod_fast(a,b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


