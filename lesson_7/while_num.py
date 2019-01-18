# while_num.py
while True:
    text = input("Введите число или стоп для выхода: ")
    # учитываем регистр:
    if text.lower() == "стоп":
        print("Выход из программы! До встречи!")
        break
    elif text == '1':
        print("Это число 1.")
    else:
        print("Что это?")
