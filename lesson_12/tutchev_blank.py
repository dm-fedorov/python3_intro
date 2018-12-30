# tutchev_blank.py
def get_html(text, img):    
    '''
    Функция для генерации html-документа.
    text: файл с текстом
    img: файл с изображением
    '''
    import urllib.request

    # здесь ваш код

    try:
        # здесь ваш код

    except Exception as error:
        print(error)        
    else:
        print("Файл создан!")      
    
if __name__ == "__main__":
    file = "http://dfedorov.spb.ru/python/files/tutchev.txt"
    pic = "http://dfedorov.spb.ru/python/files/tutchev.jpg"
    get_html(file, pic)   
    
