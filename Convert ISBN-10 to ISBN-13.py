def isbn_converter(isbn):
    isbn = '978-' + isbn[:-1]
    twelve_digits = 0
    for z, x in enumerate(''.join(isbn.split('-'))):
        if z % 2 == 0 :
            twelve_digits += int(x) * 1
        else:
            twelve_digits += int(x) * 3
    twelve_digits = twelve_digits % 10
    if twelve_digits == 0:
        return isbn+str(twelve_digits)
    else:
        return isbn+str(10-twelve_digits)