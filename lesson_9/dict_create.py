# dict_create.py
from pprint import pprint
D = dict(name='mel', age=45)
print(D)
print(list(D.values()))
print(list(D.items()))
D['about'] = {'index': 67, 'id': 54, 'age': 43}
pprint(D)
del D['name']
pprint(D)
print(list(D.keys()))
pprint(D)
print(D['about']['index'])
