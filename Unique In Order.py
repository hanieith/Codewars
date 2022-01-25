def unique_in_order(iterable):
    if len(iterable) == 0:
        return []
    else:
        result = list()
        pers = iterable[0]
        result.append(pers)
        for i in iterable:
            if pers == i:
                continue
            else:
                pers = i
                result.append(i)
    return result