# пример для проведения декомпиляции
x = 30
y = 62
z = x + y
# python3.7 -m dis test.py

'''
  1           0 LOAD_CONST               0 (30)
              2 STORE_NAME               0 (x)

  2           4 LOAD_CONST               1 (62)
              6 STORE_NAME               1 (y)

  3           8 LOAD_NAME                0 (x)
             10 LOAD_NAME                1 (y)
             12 BINARY_ADD
             14 STORE_NAME               2 (z)
             16 LOAD_CONST               2 (None)
             18 RETURN_VALUE

'''
