# sum_num.py
def add(a, b):
    return a + b

def mul(a, b):
    return a * b

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

print("Сумма введенных чисел:", add(add(num1, num2), num3))
print("Произведение введенных чисел:", mul(mul(num1, num2), num3))


