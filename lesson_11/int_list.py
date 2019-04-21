# int_list.py
class IntList:
    def __init__(self, initial_list=[]):
        if not isinstance(initial_list, list):            
            raise TypeError("Жду список в качестве входного значения.")            
        
        for element in initial_list:
            self._check(element)
        
        self.elements = initial_list[:]
    
    def _check(self, element):
        if not isinstance(element, int):
            raise TypeError("Список может включать только целые числа.")
    
    def __setitem__(self, i, element):
        self._check(element)
        self.elements[i] = element
        
    def __getitem__(self, i):
        return self.elements[i]
    
    def __len__(self):
        return len(self.elements) 

  