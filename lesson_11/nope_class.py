# nope_class.py
class Nope:
    #def __bool__(self):
    #    return False
    pass
    
    
# по умолчанию проверяется значение __len__ 
print(bool(Nope()))
