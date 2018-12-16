# my_sin_fun.py
from operator import sub

def fun(x): 
    import math
    return math.sqrt(sub(1, pow(math.sin(x), 2)))
  
if __name__ == "__main__":
    x = int(input("Введите значение x: "))
    print("Функция:", fun(x))

