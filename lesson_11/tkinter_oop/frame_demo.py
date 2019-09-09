# Эта программа создает надписи в двух разных рамках.

import tkinter

class MyGUI:
    def __init__(self):
        # Создать элемент интерфейса главного окна.
        self.main_window = tkinter.Tk()

        # Создать две рамки, одну для верхней части 
        # окна, и другую для нижней части.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Создать три элемента интерфейса Label
        # для верхней рамки.
        self.label1 = tkinter.Label(self.top_frame,
                                    text='Мигнуть')
        self.label2 = tkinter.Label(self.top_frame,
                                    text='Моргнуть')
        self.label3 = tkinter.Label(self.top_frame,
                                    text='Кивнуть')

        # Упаковать надписи, расположенные в верхней рамке.
        # Применить аргумент side='top', чтобы их
        # расположить один под другим.
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')

        # Создать три элемента интерфейса Label
        # для нижней рамки.
        self.label4 = tkinter.Label(self.bottom_frame,
                                    text='Мигнуть')
        self.label5 = tkinter.Label(self.bottom_frame,
                                    text='Моргнуть')
        self.label6 = tkinter.Label(self.bottom_frame,
                                    text='Кивнуть')

        # Упаковать надписи, расположенные в нижней рамке.
        # Применить аргумент side='left', чтобы их
        # расположить горизонтально слева рамки.
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        # Да, и мы также должны упаковать рамки!
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()