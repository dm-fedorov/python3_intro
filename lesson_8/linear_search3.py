# linear_search3.py
def linear_search(lst, value):
    '''
    Реализация алгоритма линейного поиска. Версия 3
    '''
    lst.append(value)
    i=0
    while lst[i] != value:
        i += 1
	
    lst.pop()

    if i == len(lst):
        return -1
    else:
        return i

if __name__ == '__main__':
    print(linear_search([2, 5, 1, -3], 5))
    print(linear_search([2, 4, 2], 2))
    print(linear_search([2, 4, 2], 3))
