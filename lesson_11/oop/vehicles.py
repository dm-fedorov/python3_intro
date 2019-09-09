# Класс Automobile содержит общие данные
# об автомобиле в на складе.

class Automobile:
    # Метод __init__method принимает аргументы для
    # фирмы-изготовителя, модели, пробега и цены. 
    # Он инициализирует атрибуты данных этими значениями.
 
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    # Следующие ниже методы являются методами-модификаторами 
    # атрибутов данных этого класса.

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    # Следующие ниже методы являются методами-получателями
    # атрибутов данных этого класса.

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price
    
# Класс Car представляет легковой автомобиль.
# Он является подклассом класса Automobile.

class Car(Automobile):
    # Метод __init__method принимает аргументы для
    # фирмы-изготовителя, модели, пробега, цены и количества дверей.

    def __init__(self, make, model, mileage, price, doors):
        # Вызвать метод __init__ надкласса и передать
        # требуемые аргументы. Обратите внимание, что мы также
        # передаем self в качестве аргумента.
        Automobile.__init__(self, make, model, mileage, price)

        # Инициализировать атрибут __doors.
        self.__doors = doors

    # Метод set_doors является методом-модификатором 
    # атрибута __doors.

    def set_doors(self, doors):
        self.__doors = doors

    # Метод get_doors является методом-получателем
    # атрибута __doors.

    def get_doors(self):
        return self.__doors

# Класс Truck представляет пикап. 
# Он является подклассом класса Automobile.

class Truck(Automobile):
    # Метод __init__ принимает аргументы для
    # изготовителя, модели, пробега, цены и типа привода пикапа.

    def __init__(self, make, model, mileage, price, drive_type):
        # Вызвать метод __init__ надкласса и передать
        # требуемые аргументы. Обратите внимание, что мы также
        # передаем self в качестве аргумента.
        Automobile.__init__(self, make, model, mileage, price)

        # Инициализировать атрибут __drive_type.
        self.__drive_type = drive_type

    # Метод set_drive_type является методом-модификатором
    # атрибута __drive_type.

    def set_drive_type(self, drive_type):
        self.__drive = drive_type

    # Метод get_drive_type является методом-получателем
    # атрибута __drive_type.

    def get_drive_type(self):
        return self.__drive_type
		
# Класс SUV представляет джип. 
# Он является подклассом класса Automobile.

class SUV(Automobile):
    # Метод __init__ принимает аргументы для
    # изготовителя, модели, пробега, цены и
    # пассажирской вместимости.

    def __init__(self, make, model, mileage, price, pass_cap):
        # Вызвать метод __init__ надкласса и передать
        # требуемые аргументы. Обратите внимание, что мы также
        # передаем self в качестве аргумента.
        Automobile.__init__(self, make, model, mileage, price)

        # Инициализировать атрибут __pass_cap.
        self.__pass_cap = pass_cap

    # Метод set_pass_cap является методом-модификатором
    # атрибутом __pass_cap.

    def set_pass_cap(self, pass_cap):
        self.__pass_cap = pass_cap

    # Метод get_pass_cap является методом-получателем
    # атрибутом __pass_cap.

    def get_pass_cap(self):
        return self.__pass_cap