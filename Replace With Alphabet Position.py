def alphabet_position(text):
    liste = list()
    for i in text.upper():
        if i.isalpha():
            z = ord(i) - 64
            liste.append(str(z))
    return ' '.join(liste)