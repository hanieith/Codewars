def is_valid_walk(walk):
    l, r, s, b = walk
    if count ('l') == count('r') and count('s') == count('b'):
        return True
    else:
        return False
