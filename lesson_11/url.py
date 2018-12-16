# url.py
import urllib.request
def url_open(url:str) -> list:
    """
    Функция возвращает список строк, прочитанный из файла на удаленном сервере.
    
    """
    lst = list()    
    try:     
        with urllib.request.urlopen(url) as webpage:
            # где webpage - файловый объект, кот. содержит информацию об открываемом файле.
            for line in webpage: 
                # преобразуем тип bytes в str с исп. кодировки utf-8
                line = line.decode('utf-8')
                line = line.strip()
                lst.append(line)
        return lst
    except Exception as e:        
        return e
        
if __name__ == '__main__':
    print(url_open("http://dfedorov.spb.ru/python3/src/romeo.txt"))
    
