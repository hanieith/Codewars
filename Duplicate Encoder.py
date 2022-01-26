def duplicate_encode(word):
    word = word.lower()
    result = [')' if word.count(i) > 1 else '(' for i in word ]
    return ''.join(result)