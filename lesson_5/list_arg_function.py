# list_arg_function.py
def add_element_to_list(a, b=[]):
    b.append(a)
    return b

print(add_element_to_list(5))
print(add_element_to_list(7))

def add_element_to_list_none(a, b=None):
    if b == None:
        b = []
    b.append(a)
    return b

print(add_element_to_list_none(5))
print(add_element_to_list_none(7))
