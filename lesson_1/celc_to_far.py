# cel_to_far.py
def mul(x, y):
    return x * y

def add(x, y):
    return x + y

def celc_to_far(celc):
    return add(mul(9/5, celc), 32)

print("Программа для перевода:", celc_to_far(45))

