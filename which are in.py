def in_array(array1, array2):
    a = list(set([i for i in array1 for z in array2 if i in z]))
    return sorted(a)