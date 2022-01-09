def highest_value(a, b):
    return sorted([a,b], key=lambda x: (sum([ord(i) for i in x])))[1]