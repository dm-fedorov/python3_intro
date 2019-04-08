# class_car1.py
# создаем класс Car
class Car:  
    def start(self):
        # переменная внутри метода:
        message = "Двигатель заведен" 
        return message

car = Car()  
# print(car.message)
# AttributeError: 'Car' object has no attribute 'message'
# не можем обратиться к переменной внутри метода

print(car.start()) # Car.start(car)
