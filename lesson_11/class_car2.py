# class_car2.py
# создаем класс Car
class Car:  
    # переменная класса:
    message1 = "Двигатель заведен"
 
    def start(self):
        message2 = "Автомобиль заведен"
        return message2
 
car = Car()  
# можем обратиться к (глобальной) переменной класса:
print(car.message1)
