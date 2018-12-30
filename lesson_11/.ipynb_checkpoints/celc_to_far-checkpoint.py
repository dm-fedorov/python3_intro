# cel_to_far.py
from operator import mul, add 

def celc_to_far(celc):
    '''
    Функция для перевода градусов по шкале Цельсия в градусы по шкале Фаренгейта.

    celc - градусы по шкале Цельсия.

    >>> celc_to_far(45)
    113.0
    '''
    return add(mul(9/5, celc), 32)

if __name__ == '__main__':    
    import doctest
    doctest.testmod()
