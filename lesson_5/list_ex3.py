# list_ex3.py
L = [3, 'hello', 7, 4, 'привет', 4, 3, -1]

if 'привет' in L:
    L.remove('привет')
else:
    L.append('привет')

print(L)

print(L.count(4))
if L.count(4) > 1:
    L.clear()

print(L)
