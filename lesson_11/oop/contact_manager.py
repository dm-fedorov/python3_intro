# Эта программа управляет контактами.
import contact
import pickle

# Глобальные константы для пунктов меню
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Глобальная константа для имени файла
FILENAME = 'contacts.dat'

# Главная функция
def main():
    # Загрузить существующий словарь контактов и
    # присвоить его переменной mycontacts.
    mycontacts = load_contacts()

    # Инициализировать переменную для выбора пользователя.
    choice = 0

    # Обрабатывать варианты выбора пунктов меню до тех пор,
    # пока пользователь не пожелает выйти из программы.
    while choice != QUIT:
        # Получить выбранный пользователем пункт меню.
        choice = get_menu_choice()

        # Обработать выбранный пункт меню.
        if choice == LOOK_UP:
            look_up(mycontacts)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)

    # Сохранить словарь mycontacts в файле.
    save_contacts(mycontacts)

def load_contacts():
    try:
        # Открыть файл contacts.dat.
        input_file = open(FILENAME, 'rb')

        # Расконсервировать словарь.
        contact_dct = pickle.load(input_file)

        # Закрыть файл phone_inventory.dat.
        input_file.close()
    except IOError:
        # CНе получилось открыть файл, поэтому
        # создать пустой словарь.
        contact_dct = {}

    # Вернуть словарь.
    return contact_dct

# Функция get_menu_choice выводит меню и получает
# проверенный на допустимость выбранный пользователем пункт.
def get_menu_choice():
    print()
    print('Меню')
    print('--------------------------------')
    print('1. Найти контакт')
    print('2. Добавить новый контакт')
    print('3. Изменить существующий контакт')
    print('4. Удалить контакт')
    print('5. Выйти из программы')
    print()

    # Получить выбранный пользователем пункт меню.
    choice = int(input('Введите выбранный пункт: '))

    # Проверить выбранный пункт на допустимость.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Введите выбранный пункт: '))

    # Вернуть выбранный пользователем пункт.
    return choice

# Функция look_up отыскивает элемент в
# заданном словаре.
def look_up(mycontacts):
    # Получить искомое имя.
    name = input('Введите имя: ')

    # Отыскать его в словаре.
    print(mycontacts.get(name, 'Это имя не найдено.'))

# Функция add добавляет новую запись в
# указанный словарь.
def add(mycontacts):
    # Получить контактную информацию.
    name = input('Имя: ')
    phone = input('Телефон: ')
    email = input('Электронный адрес: ')

    # Создать именованную запись с объектом Contact.
    entry = contact.Contact(name, phone, email)

    # Если имя в словаре не существует, то
    # добавить его в качестве ключа со связанным с ним
    # значением в виде объекта.
    if name not in mycontacts:
        mycontacts[name] = entry
        print('Запись добавлена.')
    else:
        print('Это имя уже существует.')

# Функция change изменяет существующую
# запись в указанном словаре.
def change(mycontacts):
    # Получить искомое имя.
    name = input('Введите имя: ')

    if name in mycontacts:
        # Получить новый телефонный номер.
        phone = input('Введите новый телефонный номер: ')

        # Получить новый электронный адрес.
        email = input('Введите новый электронный адрес: ')

        # Создать именованную запись с объектом Contact.
        entry = contact.Contact(name, phone, email)

        # Обновить запись.
        mycontacts[name] = entry
        print('Информация обновлена.')
    else:
        print('Это имя не найдено.')

# Функция delete удаляет запись
# из указанного словаря.
def delete(mycontacts):
    # Получить искомое имя.
    name = input('Введите имя: ')

    # Если имя не найдено, то удалить запись.
    if name in mycontacts:
        del mycontacts[name]
        print('Запись удалена.')
    else:
        print('Это имя не найдено.')

# Функция save_contacts консервирует указанный
# объект и сохраняет его в файле контактов.
def save_contacts(mycontacts):
    # Открыть файл для записи.
    output_file = open(FILENAME, 'wb')

    # Законсервировать словарь и сохранить его.
    pickle.dump(mycontacts, output_file)

    # Закрыть файл.
    output_file.close()

# Вызвать главную функцию.
main()