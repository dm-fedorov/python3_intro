# dog3.py
# Создаем описание собаки
class Dog:    
    # Конструктор
    # Вызывается в момент создания объекта этого типа
    def __init__(self, new_name='Собака без имени'):        
        self._name = new_name
    # Можем в любой момент вызвать этот метод и изменить имя:
    def set_name(self, new_name):
        self._name = new_name
    # Можем в любой момент вызвать этот метод и узнать имя:
    def get_name(self):
        return self._name

# Создаем конкретную собаку
my_dog = Dog("Тузик")
# Вывести имя собаки, убедиться, что оно было установлено
print(my_dog.get_name())
# Изменили имя собаки
my_dog.set_name("Шарик")
# Посмотрели изменения
print(my_dog.get_name())

