# get_int.py
def get_int(msg):
    while True:
        try:
            x = int(input(msg))
            return x            
        except ValueError:
            print("Ошибка преобразования типа. Повторите ввод")

if __name__ == "__main__":
    print(get_int("Введите целое число: "))
