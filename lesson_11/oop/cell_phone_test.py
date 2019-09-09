# Эта программа тестирует класс CellPhone.

import cellphone

def main():
    # Получить данные о телефоне.
    man = input('Введите производителя: ')
    mod = input('Введите номер модели: ')
    retail = float(input('Введите розничную цену: '))

    # Создать экземпляр класса CellPhone.
    phone = cellphone.CellPhone(man, mod, retail)

    # Показать введенные данные.
    print('Вот введенные Вами данные:')
    print('Производитель:', phone.get_manufact())
    print('Номер модели:', phone.get_model())
    print('Розничная цена: $', format(phone.get_retail_price(), ',.2f'), sep='')

# Вызвать главную функцию.
main()