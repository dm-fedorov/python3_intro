# check_zero_try.py
def try_div(x):
    if x:
        return 5 / x
    else:
        raise ZeroDivisionError    # генерируем объект ZeroDivisionError
        
def math_function(a):
    import math
    return try_div(a) * math.pi

if __name__ == '__main__':
    try:
        print(math_function(5))        
        print(math_function(0))
    except ZeroDivisionError:
        print('В процессе работы программы произошла ошибка деления на ноль')
