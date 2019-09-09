# Эта программа показывает два элемента Label с текстом.

import tkinter

class MyGUI:
    def __init__(self):
        # Создать элемент интерфейса главного окна.
        self.main_window = tkinter.Tk()

        # Создать два элемента интерфейса Label.
        self.label1 = tkinter.Label(self.main_window,
                                    text='Привет, мир!')
        self.label2 = tkinter.Label(self.main_window,
                        text='Это моя программа с ГИП.')

        # Вызвать метод pack обоих элементов интерфейса Label.
        self.label1.pack()
        self.label2.pack()

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()