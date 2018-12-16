# prog1.py
pH = float(input("Введите pH: "))

if pH == 7.0:
    print(pH, "Вода")
elif 7.36 < pH < 7.44:
    print(pH, "Кровь")
else:
    print("Что это?!")
