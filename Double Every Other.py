#Write a function that doubles every second integer in a list starting from the left.
def double_every_other(l):
    return [x * 2 if z % 2 else x for z, x in enumerate(l)]