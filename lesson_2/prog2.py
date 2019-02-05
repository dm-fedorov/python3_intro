# prog2.py
value = input("Введите pH: ")
if value:
    pH = float(value)
    if pH == 7.0:
        print("Вода")
    elif 7.36 < pH < 7.44:
        print("Кровь")
    else:
        print("Что это?!")
else:
    print("Введите значение pH!")
