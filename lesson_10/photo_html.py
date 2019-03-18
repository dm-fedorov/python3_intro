# photo_html.py
def get_html_from_dir_photo(mydir):
    import os
    HTML_BEGIN = '''
            <!DOCTYPE html>
    <html>
        <head>
           <meta charset="utf-8">
           <title>Фотогалерея</title>
        </head>
        <body>'''

    HTML_IMG = '''<p><img src='./photo/{img}' width="500" height="255" alt="Картинка"></p>'''
    HTML_END = '''</body> </html>'''
    
    try:
        with open('photo.html', 'w', encoding='utf-8') as f:
            f.write(HTML_BEGIN)
            if os.path.exists(mydir): # проверяем наличие директории:           
                for img in os.listdir(mydir):
                    f.write(HTML_IMG.format(img=img))                
                f.write(HTML_END)

                # открываем в браузере созданный html-файл:
                import webbrowser                
                webbrowser.open('photo.html')
            else:
                print("Директория не найдена! Файл не создан!")
    except Exception as error:
        print(error)
    else:
        print("Файл создан!")
        
if __name__ == '__main__':
    get_html_from_dir_photo('photo')  

    
