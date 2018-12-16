# test_prog2.py
def func(v1, v2, v3):
    '''Вычисляет среднее арифметическое трех чисел.

    >>> func(20, 30, 70)
    40.0

    >>> func(1, 5, 8)
    4.667

    '''
    return round((v1+v2+v3)/3, 3)

import doctest
# автоматически проверяет тесты в документации
doctest.testmod()
