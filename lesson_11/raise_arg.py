# raise_arg.py
class AgeError(Exception): 
    pass

def get_age():
    age = int(input("Укажите ваш возраст: "))
    if age < 0:
        #return 'Error'
        raise AgeError("{0} is not a valid age".format(age))        
    return age

if __name__ == '__main__':
    get_age()
