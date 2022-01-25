def wave(people):
    result = list()
    for z, x in enumerate(people):
        if x == ' ':
            continue
        result.append(people[:z] + x.upper() + people[z+1:])
    return result