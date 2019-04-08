# class_car3.py
# создаем класс Car
class Car:  
    def __init__(self):
        print("Двигатель заведен")
        self.name = "corolla"
        self._make = "toyota"
        self._model = 1999
        
car = Car()  
# можем обратиться к переменной объекта:
print(car.name)
