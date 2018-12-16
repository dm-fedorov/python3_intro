# arg1.py
# ключевые аргументы
def func(a, b=5, c=10): 
    print('a равно', a, ', b равно', b, ', а c равно', c) 

print(func(3, 7)) 
print(func(25, c=24)) 
print(func(c=50, a=100)) 
