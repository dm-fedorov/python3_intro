# keywords.py
def total(init=0, *numbers, **keywords):    
    """
    Когда мы объявляем параметр со звёздочкой (например, *param),
    все позиционные аргументы начиная с этой позиции и до конца
    будут собраны в кортеж под именем param. Аналогично, когда мы
    объявляем параметры с двумя звёздочками (**param), все ключевые
    аргументы начиная с этой позиции и до конца будут собраны в словарь
    под именем param.
    """
    # именованный параметр позволяет первый аргумент задавать
    # в качестве начального значения
    count = init # начальное значение счетчика суммы чисел 
    for number in numbers: 
        count = count + number # count += number
    for key in keywords: 
        count = count + keywords[key] 
    return count 

if __name__ == '__main__':
    print(total()) # init=0
    print(total(init=7)) # init=7
    print(total(2)) # init=2
    print(total(2, 1))
    print(total(2, 1, num=5))
    print(total(10, 1, 2, num1=4, num2=6)) 

