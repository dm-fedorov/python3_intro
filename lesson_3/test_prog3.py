# test_prog3.py
from operator import add

def fun(x):
    """Вычисляет значение функции.
    >>> fun(1)
    5
    >>> fun(3)
    145
    """ 
    return add(pow(x, 4), pow(4, x))

import doctest
doctest.testmod()
