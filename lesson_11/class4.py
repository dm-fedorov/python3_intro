# class4.py
class Person:
    def __init__(self, name='Человек без имени'):
        self.name = name
        self.age = 0
    def say(self):
        print("{0} говорит".format(self.name))

class Employee(Person):
    def __init__(self, name):
        Person.__init__(self)
        self.job_title = 'Безработный'
    def __str__(self):
        return '{0} {1}'.format(self.name, self.job_title)                
    def set_job(self, job_title='Безработный'):
        self.job_title = job_title        
    def get_job(self):
        print(self.name, self.job_title)    

class Builder(Employee):
    def __init__(self, name):
        Employee.__init__(self, name)
        self.experience = 'Без опыта'
    def __str__(self):
        return '{0} {1} {2}'.format(self.name, self.job_title, self.experience)            
    def set_experience(self, experience='Без опыта'):
        self.experience = experience        
    def get_experience(self):
        print(self.name, self.experience)     

person = Person('Иван')

emp = Employee('Игорь')
print(emp)

b = Builder('Петр')
print(b)
