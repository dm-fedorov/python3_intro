# fun_class_dog.py
def info_obj(obj):
    """ Отображает на экране поля объекта """
    # поля объекта могут обновиться, поэтому придется менять функцию:
    # print(dog.name)

    # обратиться к полям через словарь:
    for i in obj.__dict__:
        print('{0} : {1}'.format(i, obj.__dict__[i]))

if __name__ == '__main__':
    import second_class_dog    
    info_obj(second_class_dog.dog1)
