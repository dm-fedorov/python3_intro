
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-


# # Глава 10. Классы и объектно-ориентированное программирование 

# ## 10.2 Классы

# ### Программа 10-1 (класс Coin, незаконченная программа)

# In[1]:


import random

# Класс Coin имитирует монету, которую
# можно подбрасывать.

class Coin:

    # Метод __init__ инициализирует
    # атрибут данных sideup значением 'Орел'.

    def __init__(self):
        self.sideup = 'Орел'

    # Метод toss генерирует случайное число
    # в диапазоне от 0 до 1. Если это число
    # равно 0, то sideup получает значение 'Орел'.
    # В противном случае sideup получает значение 'Решка'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Орел'
        else:
            self.sideup = 'Решка'

    # Метод get_sideup возвращает значение,
    # на которое ссылается sideup.

    def get_sideup(self):
        return self.sideup


# ### Программа 10-2 (coin_demo1.py)

# In[47]:


import random

# Класс Coin имитирует монету, которую
# можно подбрасывать.

class Coin:

    # Метод __init__ инициализирует
    # атрибут данных sideup значением 'Орел'.

    def __init__(self):
        self.sideup = 'Орел'

    # Метод toss генерирует случайное число
    # в диапазоне от 0 до 1. Если это число
    # равно 0, то sideup получает значение 'Орел'.
    # В противном случае sideup получает значение 'Решка'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Орел'
        else:
            self.sideup = 'Решка'

    # Метод get_sideup возвращает значение,
    # на которое ссылается sideup.

    def get_sideup(self):
        return self.sideup

# Главная функция.
def main():
    # Создать объект на основе класса Coin.
    my_coin = Coin()

    # Показать обращенную вверх сторону монеты.
    print('Эта сторона обращена вверх:', my_coin.get_sideup())

    # Подбросить монету.
    print('Подбрасываю монету...')
    my_coin.toss()

    # Показать обращенную вверх сторону монеты.
    print('Эта сторона обращена вверх:', my_coin.get_sideup())

# Вызвать главную функцию.
main()


# ### Программа 10-3 (coin_demo2.py)

# In[48]:


import random

# Класс Coin имитирует монету, которую
# можно подбрасывать.

class Coin:

    # Метод __init__ инициализирует
    # атрибут данных sideup значением 'Орел'.

    def __init__(self):
        self.sideup = 'Орел'

    # Метод toss генерирует случайное число
    # в диапазоне от 0 до 1. Если это число
    # равно 0, то sideup получает значение 'Орел'.
    # В противном случае sideup получает значение 'Решка'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Орел'
        else:
            self.sideup = 'Решка'

    # Метод get_sideup возвращает значение,
    # на которое ссылается sideup.

    def get_sideup(self):
        return self.sideup

# Главная функция.
def main():
    # Создать объект на основе класса Coin.
    my_coin = Coin()

    # Показать обращенную вверх сторону монеты.
    print('Эта сторона обращена вверх:', my_coin.get_sideup())

    # Подбросить монету.
    print('Подбрасываю монету...')
    my_coin.toss()

    # Но теперь я обману! В этом объекте 
    # я собираюсь напрямую поменять  
    # значение атрибута sideup на 'Орел'.
    my_coin.sideup = 'Орел'

    # Показать обращенную вверх сторону монеты.
    print('Эта сторона обращена вверх:', my_coin.get_sideup())

# Вызвать главную функцию.
main()


# ### Программа 10-4 (coin_demo3.py)

# In[46]:


import random

# Класс Coin имитирует монету, которую
# можно подбрасывать.

class Coin:

    # Метод __init__ инициализирует
    # атрибут данных __sideup значением 'Орел'.

    def __init__(self):
        self.__sideup = 'Орел'

    # Метод toss генерирует случайное число
    # в диапазоне от 0 до 1. Если это число
    # равно 0, то __sideup получает значение 'Орел'.
    # В противном случае sideup получает значение 'Решка'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Орел'
        else:
            self.__sideup = 'Решка'

    # Метод get_sideup возвращает значение,
    # на которое ссылается __sideup.

    def get_sideup(self):
        return self.__sideup

# Главная функция.
def main():
    # Создать объект на основе класса Coin.
    my_coin = Coin()

    # Показать обращенную вверх сторону монеты.
    print('Эта сторона обращена вверх:', my_coin.get_sideup())

    # Подбросить монету.
    print('Собираюсь подбросить монету десять раз:')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

# Вызвать главную функцию.
main()


# ### Программа 10-5 (coin.py)

# In[29]:


import random

# Класс Coin имитирует монету, которую
# можно подбрасывать (теперь это модуль, который хранится в файле).

class Coin:

    # Метод __init__ инициализирует
    # атрибут данных __sideup значением 'Орел'.

    def __init__(self):
        self.__sideup = 'Орел'

    # Метод toss генерирует случайное число
    # в диапазоне от 0 до 1. Если это число
    # равно 0, то __sideup получает значение 'Орел'.
    # В противном случае sideup получает значение 'Решка'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Орел'
        else:
            self.__sideup = 'Решка'

    # Метод get_sideup возвращает значение,
    # на которое ссылается __sideup.

    def get_sideup(self):
        return self.__sideup


# ### Программа 10-6 (coin_demo4.py)

# In[45]:


# Эта программа импортирует модуль coin и
# создает экземпляр класса Coin.

import coin

def main():
    # Создать объект на основе класса Coin.
    my_coin = coin.Coin()

    # Показать обращенную вверх сторону монеты.
    print('Эта сторона обращена вверх:', my_coin.get_sideup())

    # Подбросить монету.
    print('Собираюсь подбросить монету десять раз:')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

# Вызвать главную функцию.
main()


# ### Программа 10-7 (bankaccount.py)

# In[33]:


# Класс BankAccount имитирует банковский счет.

class BankAccount:

    # Метод __init__ принимает аргумент 
    # с остатком на счете. 
    # Он присваивается атрибуту __balance.

    def __init__(self, bal):
        self.__balance = bal

    # Метод deposit вносит 
    # на счет вклад.

    def deposit(self, amount):
        self.__balance += amount

    # Метод withdraw снимает сумму
    # со счета.

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Ошибка: недостаточно средств')

    # Метод get_balance возвращает
    # остаток средств на счете.

    def get_balance(self):
        return self.__balance


# ### Программа 10-8 (account_test.py)

# In[37]:


# Эта программа демонстрирует класс BankAccount.

import bankaccount

def main():
    # Получить начальный остаток.
    start_bal = float(input('Введите свой начальный остаток: '))

    # Создать объект BankAccount.
    savings = bankaccount.BankAccount(start_bal)

    # Внести на счет зарплату пользователя.
    pay = float(input('Сколько Вы получили на этой неделе? '))
    print('Вношу эту сумму на Ваш счет.')
    savings.deposit(pay)

    # Показать остаток.
    print('Ваш остаток на банковском счете составляет $',
          format(savings.get_balance(), ',.2f'),
          sep='')

    # Получить сумму для снятия с банковского счета.
    cash = float(input('Какую сумму Вы желаете снять со счета? '))
    print('Снимаю эту сумму с Вашего банковского счета.')
    savings.withdraw(cash)

    # Показать остаток.
    print('Ваш остаток на банковском счете составляет $',
          format(savings.get_balance(), ',.2f'),
          sep='')

# Вызвать главную функцию.
main()


# ### Программа 10-9 (bankaccount2.py)

# In[39]:


# Класс BankAccount имитирует банковский счет.

class BankAccount:

    # Метод __init__ принимает аргумент 
    # с остатком на счете. 
    # Он присваивается атрибуту __balance.

    def __init__(self, bal):
        self.__balance = bal

    # Метод deposit вносит 
    # на счет вклад.

    def deposit(self, amount):
        self.__balance += amount

    # Метод withdraw снимает сумму
    # со счета.

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Ошибка: недостаточно средств')

    # Метод get_balance возвращает
    # остаток средств на счете.

    def get_balance(self):
        return self.__balance
    
    # Метод __str__ возвращает строковое
    # значение, сообщающее о состоянии объекта.

    def __str__(self):
        return 'Остаток составляет $' + format(self.__balance, ',.2f')


# ### Программа 10-10 (account_test2.py)

# In[40]:


# Эта программа демонстрирует класс BankAccount
# с добавленным в него методом __str__.

import bankaccount2

def main():
    # Получить начальный остаток.
    start_bal = float(input('Введите свой начальный остаток: '))

    # Создать объект BankAccount.
    savings = bankaccount2.BankAccount(start_bal)

    # Внести на счет зарплату пользователя.
    pay = float(input('Сколько Вы получили на этой неделе? '))
    print('Вношу эту сумму на Ваш счет.')
    savings.deposit(pay)

    # Показать остаток.
    print(savings)

    # Получить сумму для снятия с банковского счета.
    cash = float(input('Какую сумму Вы желаете снять со счета? '))
    print('Снимаю эту сумму с Вашего банковского счета.')
    savings.withdraw(cash)

    # Показать остаток.
    print(savings)

# Вызвать главную функцию.
main()


# ## 10.3 Работа с экземплярами

# ### Программа 10-11 (coin_demo5.py)

# In[50]:


# Эта программа импортирует имитационный модуль и
# создает три экземпляра класса Coin.

import coin

def main():
    # Создать три объекта класса Coin.
    coin1 = coin.Coin()
    coin2 = coin.Coin()
    coin3 = coin.Coin()

    # Показать обращенную вверх сторону каждой монеты.
    print('Вот три монеты, у которых эти стороны обращены вверх:')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()

    # Подбросить монету.
    print('Подбрасываю все три монеты...')
    print()
    coin1.toss()
    coin2.toss()
    coin3.toss()

    # Показать обращенную вверх сторону каждой монеты.
    print('Теперь обращены вверх вот эти стороны:')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()

# Вызвать главную функцию.
main()


# ### Программа 10-12 (cellphone.py)

# In[52]:


# Класс CellPhone содержит данные о сотовом телефоне.

class CellPhone:

    # Метод __init__ инициализирует атрибуты.

    def __init__(self, manufact, model, price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = price

    # Метод set_manufact принимает аргумент для
    # производителя телефона.

    def set_manufact(self, manufact):
        self.__manufact = manufact

    # Метод set_model принимает аргумент для
    # номера модели телефона.

    def set_model(self, model):
        self.__model = model

    # Метод set_retail_price принимает аргумент для
    # розничной цены телефона.

    def set_retail_price(self, price):
        self.__retail_price = price

    # Метод get_manufact возвращает
    # производителя телефона.

    def get_manufact(self):
        return self.__manufact

    # Метод get_model возвращает
    # номер модели телефона.

    def get_model(self):
        return self.__model

    # Метод get_retail_price возвращает
    # розничную цену телефона.

    def get_retail_price(self):
        return self.__retail_price


# ### Программа 10-13 (cell_phone_test.py)

# In[53]:


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


# ### Программа 10-14 (cell_phone_list.py)

# In[54]:


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


# ### Программа 10-15 (coin_argument.py)

# In[58]:


# Эта программа передает объект Coin
# в качестве аргумента в функцию.
import coin

# Главная функция
def main():
    # Создать объект Coin.
    my_coin = coin.Coin()

    # Эта инструкция покажет 'Орел'.
    print(my_coin.get_sideup())

    # Передать объект в функцию flip.
    flip(my_coin)

    # Эта инструкция может показать 'Орел' 
    # либо 'Решка'.
    print(my_coin.get_sideup())

# Функция flip подбрасывает монету.
def flip(coin_obj):
    coin_obj.toss()

# Вызвать главную функцию.
main()


# ### Программа 10-16 (pickle_cellphone.py)

# In[59]:


# Эта программа консервирует объекты CellPhone.
import pickle
import cellphone

# Константа для имени файла.
FILENAME = 'cellphones.dat'

def main():
    # Инициализировать переменную для управления циклом.
    again = 'д'

    # Открыть файл.
    output_file = open(FILENAME, 'wb')

    # Получить данные от пользователя.
    while again.lower() == 'д':
        # Получить данные о сотовом телефоне.
        man = input('Введите производителя: ')
        mod = input('Введите номер модели: ')
        retail = float(input('Введите розничную цену: '))

        # Создать объект CellPhone.
        phone = cellphone.CellPhone(man, mod, retail)

        # Законсервировать объект и записать его в файл.
        pickle.dump(phone, output_file)

        # Получить еще один элемент данных?
        again = input('Введете еще один элемент данных? (д/н): ')

    # Закрыть файл.
    output_file.close()
    print('Данные записаны в', FILENAME)

# Вызвать главную функцию.
main()


# ### Программа 10-17 (unpickle_cellphone.py)

# In[60]:


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


# ### Программа 10-18 (contact.py)

# In[61]:


# Класс Contact содержит контактную информацию.

class Contact:
    # Метод __init__ инициализирует атрибуты.
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email

    # Метод set_name устанавливает атрибут name.
    def set_name(self, name):
        self.__name = name

    # Метод set_phone method устанавливает атрибут phone.
    def set_phone(self, phone):
        self.__phone = phone

    # Метод set_email устанавливает атрибут email.
    def set_email(self, email):
        self.__email = email

    # Метод get_name возвращает атрибут name.
    def get_name(self):
        return self.__name

    # Метод get_phone возвращает атрибут phone.
    def get_phone(self):
        return self.__phone

    # Метод get_email возвращает атрибут email.
    def get_email(self):
        return self.__email

    # Метод __str__ возвращает состояние объекта
    # в виде строкового значения.
    def __str__(self):
        return "Имя: " + self.__name +                "\nТелефон: " + self.__phone +                "\nЭлектронная почта: " + self.__email


# ### Программа 10-19 (contact_manager.py)

# In[66]:


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


# ## 10.4 Приемы конструирования классов

# ### Программа 10-20 (customer.py)

# In[68]:


# Класс Customer
class Customer:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone


# ### Программа 10-21 (car.py)

# In[69]:


# Класс Car
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year


# ### Программа 10-22 (servicequote.py)

# In[70]:


# Константа для ставки налога с продаж
TAX_RATE = 0.05

# Класс ServiceQuote
class ServiceQuote:
    def __init__(self, pcharge, lcharge):
        self.__parts_charges = pcharge
        self.__labor_charges = lcharge

    def set_parts_charges(self, pcharge):
        self.__parts_charges = pcharge

    def set_labor_charges(self, lcharge):
        self.__labor_charges = lcharge

    def get_parts_charges(self):
        return self.__parts_charges

    def get_labor_charges(self):
        return self.__labor_charges

    def get_sales_tax(self):
        return __parts_charges * TAX_RATE

    def get_total_charges(self):
        return __parts_charges + __labor_charges +                  (__parts_charges * TAX_RATE)

