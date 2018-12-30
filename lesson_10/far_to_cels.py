# far_to_cels.py
from operator import mul, sub 
def far_to_cels(far):
    '''
    Функция для перевода градусов по шкале Фаренгейта в градусы по шкале Цельсия.

    far - градусы по шкале Фаренгейта.

    >>> far_to_cels(444)
    228.89
    '''
    return round(mul(5/9, sub(far, 32)), 2)

if __name__ == '__main__':    
    import doctest
    doctest.testmod()
