# Эта программа чертит дугу на элементе Canvas.
import tkinter

class MyGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать элемент Canvas.
        self.canvas = tkinter.Canvas(self.main_window, 
                                     width=200, height=200)
        # Нарисовать дугу.
        self.canvas.create_arc(10, 10, 190, 190, start=45, extent=30)
 
        # Упаковать холст.
        self.canvas.pack()
 
        # Запустить главный цикл.
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()