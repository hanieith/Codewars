def zero(n = None): return 0 if not n else n(0)
def one(n = None): return 1 if not n else n(1)
def two(n = None): return 2 if not n else n(2)
def three(n = None): return 3 if not n else n(3)
def four(n = None): return 4 if not n else n(4)
def five(n = None): return 5 if not n else n(5)
def six(n = None): return 6 if not n else n(6)
def seven(n = None): return 7 if not n else n(7)
def eight(n = None): return 8 if not n else n(8)
def nine(n = None): return 9 if not n else n(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda  x: x*y
def divided_by(y): return lambda  x: x//y

print(seven(plus(five())))