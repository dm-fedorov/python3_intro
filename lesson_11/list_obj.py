# list_obj.py
class Point: 
    def __init__(self, x=0, y=0):        
        self.x = x
        self.y = y        

    def set(self, x, y):        
        self.x = x
        self.y = y

    def get(self):
        return self.x, self.y
    # специальный метод:
    def __repr__(self):
        return 'Точка с координатами ({0},{1})'.format(self.x, self.y)

pt1 = Point()
pt2 = Point(3, 5)
pt3 = Point(1, 0)
pt4 = Point(8, 0)
pt5 = Point(4, 7)

# формируем список из объектов типа Point
L = list()
L.append(pt1)
L.append(pt2)
L.append(pt3)
L.append(pt4)
L.append(pt5)

print(L)


