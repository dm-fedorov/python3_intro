# Эта программа показывает надпись с текстом.

import tkinter

class MyGUI:
    def __init__(self):
        # Создать элемент интерфейса главного окна.
        self.main_window = tkinter.Tk()

        # Создать элемент интерфейса Label, содержащий
        # надпись 'Привет, Мир!'
        self.label = tkinter.Label(self.main_window,
                                   text='Привет, мир!')

        # Вызвать метод pack  элемента интерфейса Label.
        self.label.pack()

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
my_gui = MyGUI() 