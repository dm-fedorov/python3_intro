# file_writeline_with.py
def file_write(file, lst):
    try:
        with open(file, 'w') as output_file:
            output_file.writelines(lst)
        print('данные записаны')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    file_write("toplist.txt", ['Привет!', ' прекрасный мир!'])
