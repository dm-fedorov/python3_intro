# list_ex1.py
L = [3, 6, 7, 4, -5, 4, 3, -1]
if sum(L) > 2:
    print('Длина списка:', len(L))

from operator import sub

print('Разность:', sub(min(L), max(L)))

if abs(sub(min(L), max(L))) > 10:
    print('Сортировка по убыванию:', sorted(L, reverse = True))
else:
    print("Разность меньше 10")
