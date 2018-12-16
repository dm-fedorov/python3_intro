# var3.py
def add(x, y):    
    return x + y

def sub(x, y):
    return x - y
    
def fun(x, y):
    return add(sub(x,y), sub(y, x))

a = 5
b = 7
print(fun(a, b))

