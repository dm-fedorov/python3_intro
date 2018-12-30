# while_num.py
while True:
    text = input("Введите число или стоп для выхода: ")
    if text == "стоп":
        print("Выход из программы! До встречи!")
        break
    elif text == '1':
        print("Число 1")
    else:
        print("Что это?!")
