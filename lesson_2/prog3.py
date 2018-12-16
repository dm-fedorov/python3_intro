# prog3.py
pH = float(input("Введите значение pH: "))

def get_ph(pH):
    if pH == 3.0:
        return "Яблочный сок"
    elif pH == 5.5:
        return "Шампунь"
    elif 9.0 < pH < 10.0:
        return "Мыло для рук"
    else:
        return "Не найдено"

print(get_ph(pH))

