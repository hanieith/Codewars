def compute_sum(n):
    suma = 0
    for i in range(n+1):
        for z in str(i):
            suma += sum(int(i) for i in z)
    return suma