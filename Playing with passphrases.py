def play_pass(s, n):
    s = list(s.lower())
    for z, x in enumerate(s):
        if x.isalpha():
            if (ord(x) + n) > 122:
                s[z] = chr(ord(x) + n - 26)
            else:
                s[z] = chr(ord(x) + n)
            if z % 2 == 0:
                s[z] = s[z].upper()
            else:
                s[z] = s[z].lower()
        if x.isdigit():
            s[z] = str(9 - int(x))
    return ''.join(s[::-1])