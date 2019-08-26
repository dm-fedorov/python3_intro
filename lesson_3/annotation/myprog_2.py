# myprog_2.py
from typing import TypeVar
Num = TypeVar('Num', int, float)

def summa(x: Num, y: Num) -> Num:
    return x + y

summa('3', '10')
summa(1, 4)
summa(1, 4.9)
summa(10, '10')
