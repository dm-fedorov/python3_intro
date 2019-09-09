# Эта программа наносит текст на элемент Canvas.
import tkinter
import tkinter.font

class MyGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать элемент Canvas.
        self.canvas = tkinter.Canvas(self.main_window, width=200, 
                                     height=200)
        # Создать объект Font.
        myfont = tkinter.font.Font(family='Helvetica', size=18, 
                                   weight='bold')
        # Показать немного текста.
        self.canvas.create_text(100, 100, text='Привет, мир!', 
                                font=myfont)
        # Упаковать холст.
        self.canvas.pack()
 
        # Запустить главный цикл.
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()