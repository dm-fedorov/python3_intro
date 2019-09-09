# Эта программа создает пять объектов CellPhone и
# сохраняет их в списке.

import cellphone

def main():
    # Получить список объектов CellPhone.
    phones = make_list()

    # Показать данные в списке.
    print('Вот введенные Вами данные:')
    display_list(phones)

# Функция make_list получает от пользователя данные 
# о пяти телефонах. Эта функция возвращает список
# объектов CellPhone, содержащих эти данные.

def make_list():
    # Создать пустой список.
    phone_list = []

    # Добавить пять объектов CellPhone в список.
    print('Введите данные о пяти телефонах.')
    for count in range(1, 6):
        # Получить данные о телефоне.
        print('Номер телефона ' + str(count) + ':')
        man = input('Введите производителя: ')
        mod = input('Введите номер модели: ')
        retail = float(input('Введите розничную цену: '))
        print()

        # Создать новый объект CellPhone в памяти и
        # присвоить его переменной phone.
        phone = cellphone.CellPhone(man, mod, retail)

        # Добавить объект в список.
        phone_list.append(phone)

    # Вернуть список.
    return phone_list

# Функция display_list принимает список с объектами
# CellPhone в качестве аргумента и показывает
# хранящиеся в каждом объекте данные.

def display_list(phone_list):
    for item in phone_list:
        print(item.get_manufact())
        print(item.get_model())
        print(item.get_retail_price())
        print()

# Вызвать главную функцию.
main()