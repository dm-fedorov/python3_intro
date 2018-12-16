# run_geron.py
from geron import geron
a = int(input("Введите значение стороны a: "))
b = int(input("Введите значение стороны b: "))
c = int(input("Введите значение стороны c: "))
print("Площадь треугольника по формуле Герона:", geron(a, b, c))

