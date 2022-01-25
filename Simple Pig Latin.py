def pig_it(text):
    result = list()
    for i in text.split():
        if i.isalpha():
            result.append(i[1:] + i[0] + 'ay')
        else:
            result.append(i)
    return ' '.join(result)