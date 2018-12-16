# myfunc_module.py
from operator import add

def func(x):
     return add(pow(x, 2), 7)

x = int(input("Введите значение: "))
print(func(x))
