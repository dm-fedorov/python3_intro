# dog4.py
class Dog:
    # Атрибуты класса доступны из всех экземпляров данного класса
    count = 0
    legs = 4    
    # Конструктор
    # Вызывается в момент создания объекта этого типа (класса)
    def __init__(self, new_name='Собака без имени'):        
        self._name = new_name
        Dog.count += 1 # увеличиваем счетчик экземпляров класса Dog
        
    # Можем в любой момент вызвать этот метод и изменить имя:
    def set_name(self, new_name):
        self._name = new_name
    # Можем в любой момент вызвать этот метод и узнать имя:
    def get_name(self):
        return self._name

# Создаем конкретную собаку
my_dog = Dog()
# Изменяем имя собаки
my_dog.set_name("Шарик")
# Сколько ног у собаки (доступ к атрибуту класса):
print('У {0}а {1} ноги'.format(my_dog.get_name(), my_dog.legs))

# Создаем еще одну конкретную собаку
her_dog = Dog("Бобик")
print('У {0}а {1} ноги'.format(her_dog.get_name(), her_dog.legs))
# Сколько экземпляров класса Dog создано:
print('создано собак:', Dog.count)
