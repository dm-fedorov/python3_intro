# arg2.py
def div(a, b):
    return a / b

def add(a, b):
    return a + b

def average(a=0, b=1, c=2):
    return div(add(add(a, b), c), 3)

print(average())
print(average(b=3))

