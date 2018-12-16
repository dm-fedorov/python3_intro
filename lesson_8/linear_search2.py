# linear_search2.py
def linear_search(lst, value):
    '''
    Реализация алгоритма линейного поиска. Версия 2
    '''
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1

if __name__ == '__main__':
    print(linear_search([2, 5, 1, -3], 5))
    print(linear_search([2, 4, 2], 2))
    print(linear_search([2, 4, 2], 3))
