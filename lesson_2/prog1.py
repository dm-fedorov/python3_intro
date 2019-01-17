# prog1.py
pH = float(input("Введите pH: "))

if pH == 7.0:
    print("Чистая вода")
elif 7.36 < pH < 7.44:
    print("Кровь")
else:
    print("Что это?!")
