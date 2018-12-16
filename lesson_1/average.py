# average.py
def div(a, b):
    return a / b

def add(a, b):
    return a + b

def average(a, b, c):
    return div(add(add(a, b), c), 3)

print('Среднее:', average(5, 6, 7))

