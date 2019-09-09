# Эта программа расконсервирует объекты CellPhone.
import pickle
import cellphone

# Константа для имени файла.
FILENAME = 'cellphones.dat'

def main():
    end_of_file = False # Для обозначения конца файла

    # Открыть файл.
    input_file = open(FILENAME, 'rb')

    # Прочитать до конца файла.
    while not end_of_file:
        try:
            # Расконсервировать следующий объект.
            phone = pickle.load(input_file)

            # Показать данные о сотовом телефоне.
            display_data(phone)
        except EOFError:
            # Установить флаг, чтобы обозначить, что
            # был достигнут конец файла.
            end_of_file = True

    # Закрыть файл.
    input_file.close()

# Функция display_data показывает данные
# из объекта CellPhone, переданного в качестве аргумента.
def display_data(phone):
    print('Производитель:', phone.get_manufact())
    print('Номер модели:', phone.get_model())
    print('Розничная цена: $',
          format(phone.get_retail_price(), ',.2f'),
          sep='')
    print()

# Вызвать главную функцию.
main()