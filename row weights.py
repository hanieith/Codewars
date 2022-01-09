def row_weights(array):
    teams = [0, 0]
    for z, x in enumerate(array):
        if z % 2 == 0:
            teams[0] += x
        else:
            teams[1] += x
    return tuple(teams)
