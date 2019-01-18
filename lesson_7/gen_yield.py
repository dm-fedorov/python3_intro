# gen_yield.py

def four():
    x = 0
    while x < 4:
        yield x # вместо return 
        x += 1

print('тип данных:', four())

for i in four():
    print(i)

print(2 in four())


