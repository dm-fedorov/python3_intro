# Эта программа соединяет несколько точек отрезками прямой.
import tkinter

class MyGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать элемента Canvas.
        self.canvas = tkinter.Canvas(self.main_window, 
                                     width=200, height=200)
        # Начертить отрезки прямой, соединяющей несколько точек.
        self.canvas.create_line(10, 10, 189, 10, 100, 189, 10, 10)

        # Упаковать холст.
        self.canvas.pack()
 
        # Запустить главный цикл.
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()