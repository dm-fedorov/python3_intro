# p_and_s.py
def mul(x, y):
    return x * y

def p(x):
    return mul(4, x)

def s(x):
    return mul(x, x)

print('Периметр:', p(6))
print('Площадь:', s(7))

