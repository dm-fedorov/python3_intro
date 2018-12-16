# file_append_with.py
def file_append(file, string):
    '''
    Добавление строки string в файл file.
    '''
    try:
        with open(file, 'a') as output_file:
            output_file.write(string)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    file_append('top.txt', "Hello!\n")    
