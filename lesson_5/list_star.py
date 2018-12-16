# list_star.py
def func(a, b, c):
    return a + b + c

if __name__ == '__main__':
    print(func(2, 4, 5))
    L = [2, 5, 7]
    # print(func(L)) 
    print(func(*L))
    print(func(2, *L[1:]))
