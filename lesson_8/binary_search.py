# binary_search.py
def binary_search(lst, value):    
    """ 
    Возвращает индекс первого встретившегося значения value в списке lst, или -1,
    если значение в списке не найдено.

    >>> binary_search([1, 3, 5, 6, 7, 8], 1)
    0

    >>> binary_search([1, 3, 5, 6, 7, 8], 10)
    -1

    >>> binary_search([1, 3, 5, 6, 7, 8], 5)
    2
    """

    i = 0
    j = len(lst) - 1

    while i != j + 1:
        m = (i + j) // 2
        if lst[m] < value:
            i = m + 1
        else:
            j = m - 1

    if 0 <= i < len(lst) and lst[i] == value:
        return i
    else:
        return -1

if __name__ == '__main__':
    import doctest
    doctest.testmod()

