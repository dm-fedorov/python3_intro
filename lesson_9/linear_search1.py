# linear_search1.py
def linear_search(lst, value):
    '''
    Реализация алгоритма линейного поиска. Версия 1
    '''
    i = 0
    while i != len(lst) and lst[i] != value:        
        i = i + 1 # i += 1
    if i == len(lst):
        return -1
    else:
        return i

if __name__ == '__main__':
    print(linear_search([2, 5, 1, -3], 5))
    print(linear_search([2, 4, 2], 2))
    print(linear_search([2, 4, 2], 3))
