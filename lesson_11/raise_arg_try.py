# raise_arg_try.py
def get_age():
    import raise_arg
    try:
        res = raise_arg.get_age()        
    except:
        res = None
    return res

if __name__ == '__main__':
    get_age():
        
    
