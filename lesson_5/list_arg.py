# list_arg.py
def f(x, l=[]):
    for i in range(x):
        l.append(i * i)
    return l

print(f(2))
print(f(3, [0, 1, 2]))
print(f(3))
