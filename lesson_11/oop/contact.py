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
        return "Имя: " + self.__name + \
               "\nТелефон: " + self.__phone + \
               "\nЭлектронная почта: " + self.__email