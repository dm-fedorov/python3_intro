# arg_list.py
def local_add_element(lst, element):
    import copy
    print('вызов local_add_element')
    # создаем глубокую копию списка
    deepcopy_lst = copy.deepcopy(lst)
    deepcopy_lst.append(element)
    print('возвращаем копию списка')
    return deepcopy_lst

def in_local_add_element(element):
    print('вызов in_local_add_element')
    lst = []
    lst.append(element)
    print('изменяем и возвращаем локальный список')
    return lst

def global_lst(element):
    print('вызов global_lst')
    global lst
    lst = []
    lst.append(element)
    print('изменяем глобальный список')
    return lst

def global_add_element(element):
    print('вызов global_add_element')
    lst.append(element)        

if __name__ == '__main__':
    lst = [4, 6]
    print('глобальный lst: ', lst)    
    print(local_add_element(lst, '5'))
    print('глобальный lst: ', lst)    
    print(in_local_add_element('5'))
    print('глобальный lst: ', lst)        
    global_lst('7')
    print('глобальный lst: ', lst)
    global_add_element('5')
    print('глобальный lst: ', lst)        
    
    
    
