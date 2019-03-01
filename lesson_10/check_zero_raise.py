# check_zero_raise.py
# программа работает с ошибкой
def try_div(x):
    if x:
        return 5 / x
    else:
        raise ZeroDivisionError    # генерируем объект ZeroDivisionError
        
def math_function(a):
    import math
    return try_div(a) * math.pi

if __name__ == '__main__':
    print(math_function(5))
    print(math_function(0))
    
