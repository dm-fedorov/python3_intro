# time_test1.py
from timeit import Timer

code1 = """\
arr1 = []
for i in range(1, 10001):
    arr1.append(str(i))
"""
t1 = Timer(stmt=code1)
print("append:", t1.repeat(repeat=3, number=2000))

code2 = """\
arr2 = [str(i) for i in range(1, 10001)]
"""
t2 = Timer(stmt=code2)
print("генератор:", t2.repeat(repeat=3, number=2000))



