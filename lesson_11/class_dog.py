# class_dog.py
# Некоторая собака:
class Dog:    
    # метод для произношения имени:
    def bark(self): # Преобразуется в полную форму Dog.bark(myDog)        
        print("Собака говорит: {0}".format(self.name))

# Конкретная собака:        
my_dog = Dog()
# определяем имя собаки
my_dog.name = "Шарик"
print(my_dog.name)
my_dog.weight = 20
my_dog.age = 3
my_dog.bark() # Преобразуется в полную форму Dog.bark(my_dog)
