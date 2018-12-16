# number_writer.py
def writer(filename, numbers):    
    import json    
    try:
        with open(filename, 'w') as f_obj:
            json.dump(numbers, f_obj)
    except Exception as e:
        print(e)

if __name__ == "__main__":    
    writer('numbers.json', [1, 3, 4, 5])
    
