# ex2.py
def symbol_string(symbol, string):
    '''
    Функция заменяет первый символ symbol в строке string.
    '''
    return symbol + string[1:]

print(symbol_string('a', 'bbbbb'))
