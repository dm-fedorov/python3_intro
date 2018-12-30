# file_err.py
# Ошибка при открытии файла
try:
    f = open('1example_text.txt')
except:
    print("Error opening file")
finally:
    try:
        f.close()
        print('(Очистка: Закрытие файла)')
    except NameError:
        pass
