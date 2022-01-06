def solve(arr):
    a = set(arr)
    x = 0
    while len(a) != len(arr):
        if arr.count(arr[x]) >= 2:
            arr.pop(x)
        else:
            x += 1
    return arr