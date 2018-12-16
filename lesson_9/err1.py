# err1.py
try:
    x = int(input("Введите число: "))
    print(5/x)
except ZeroDivisionError:
    print("Ошибка деления на нуль")
except ValueError:
    print("Ошибка преобразования типов")
