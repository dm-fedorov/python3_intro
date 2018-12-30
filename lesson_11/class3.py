# class3.py
class Person:
    def __init__(self, name='Человек без имени'):
        self.name = name
        self.age = 0
    def __str__(self):
        return '{}'.format(self.name)                
    def say(self):
        print("{} говорит".format(self.name))

class Employee(Person):
    def __init__(self, name='Работник без имени'):
        Person.__init__(self, name=name)
        self.job_title = 'Безработный'
    def __str__(self):
        return '{0} {1}'.format(self.name, self.job_title)                
    def set_job(self, job_title):
        self.job_title = job_title        
    def get_job(self):
        print(self.name, self.job_title)    
    
class Customer(Person):
    def __init__(self, name='Покупатель без имени'):
        Person.__init__(self, name=name)
        self.email = 'Нет почты'
    def __str__(self):
        return '{0} {1}'.format(self.name, self.email)
    def set_email(self, email):
        self.email = email        
    def get_email(self):
        print(self.name, self.email)

person = Person('Иван')
print(person)

emp = Employee('Игорь')
print(emp)

cust = Customer('Петр')
print(cust)
