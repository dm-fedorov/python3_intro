# tutchev.py
def get_html(text, img):    
    '''
    Функция для генерации html-документа.
    text: файл с текстом
    img: файл с изображением
    '''    
    import urllib.request

    HTML_BEGIN = '''
            <!DOCTYPE html>
    <html>
        <head>
           <meta charset="utf-8">
           <title>Стихи</title>
        </head>
        <body>'''
    
    HTML_END = '''
      <p><img src={img} alt="Тютчев"></p>
        </body>
    </html>'''    
    try:
        with open('tutchev.html', 'w', encoding='utf-8') as f:
            f.write(HTML_BEGIN)            
            with urllib.request.urlopen(text) as webpage:
                for line in webpage:                    
                    line = line.decode('utf-8')
                    line = line.strip()
                    f.write(line)
                    f.write("<br>")              
            f.write(HTML_END.format(img=img))            
            # открываем в браузере созданный html-файл:
            import webbrowser
            webbrowser.open('tutchev.html')

    except Exception as error:
        print(error)        
    else:
        print("Файл создан!")

if __name__ == "__main__":
    file = "http://dfedorov.spb.ru/python/files/tutchev.txt"
    pic = "http://dfedorov.spb.ru/python/files/tutchev.jpg"
    get_html(file, pic)   

    
