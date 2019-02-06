# histogram.py
def histogram(s):
    '''
    Функция для подсчета встречаемости элементов в коллекции s.
    '''
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

if __name__ == "__main__":
    print(histogram("sdfs"))
    print(histogram(['aaa', 'bbb', 'aaa', 'bbb', 'c']))
