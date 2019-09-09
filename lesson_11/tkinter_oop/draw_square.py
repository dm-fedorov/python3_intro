# Эта программа чертит прямоугольник на элементе Canvas.
import tkinter

class MyGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать элемент Canvas.
        self.canvas = tkinter.Canvas(self.main_window, 
                                     width=200, height=200)
        # Нарисовать прямоугольник.
        self.canvas.create_rectangle(20, 20, 180, 180)
        
        # Упаковать холст.
        self.canvas.pack()
 
        # Запустить главный цикл.
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()