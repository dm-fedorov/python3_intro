# prog2.py
value = input("Введите pH: ")
if len(value) > 0:
    pH = float(value)
    if pH == 7.0:
        print(pH, "Вода")
    elif 7.36 < pH < 7.44:
        print(pH, "Кровь")
    else:
        print("Что это?!")
else:
    print("Введите значение pH!")
