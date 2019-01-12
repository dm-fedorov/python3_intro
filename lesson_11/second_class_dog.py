# second_class_dog.py
class Dog:
    pass

dog1 = Dog()

# атрибуты объекта добавляются динамически по аналогии со словарями:
dog1.name = "Шарик"
dog1.age = 2

if __name__ == '__main__':
    print(dog1.age)
    # посмотреть атрибуты объекта dog1:
    print(dog1.__dict__)
