# myfunc_module2.py
from operator import add
def func(x):
     return add(pow(x, 2), 7)

if __name__ == "__main__":
   x = int(input("Введите значение: "))
   print(func(x))

