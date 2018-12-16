# format_str.py
def f1(var1, var2):
    return var1 + ' и ' + var2

def f2(var1, var2):
    return '{0} и {1}'.format(var1, var2)

# с версии 3.6:
def f3(var1, var2):
    return f'{var1} и {var2}'

if __name__ == '__main__':
    print(f1('мир', 'труд'))
    print(f2('мир', 'труд'))
    print(f3('мир', 'труд'))
