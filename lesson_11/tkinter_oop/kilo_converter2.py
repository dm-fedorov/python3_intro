# Эта программа конвертирует расстояния в километрах
# в мили. Полученный результат выводится 
# в элемент Label в главном окне.

import tkinter

class KiloConverterGUI:
    def __init__(self):

        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать три рамки, чтобы сгруппировать элементы интерфейса.
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Создать элементы интерфейса для верхней рамки.
        self.prompt_label = tkinter.Label(self.top_frame,
                    text='Введите расстояние в километрах:')
        self.kilo_entry = tkinter.Entry(self.top_frame,
                                        width=10)

        # Упаковать элементы верхней рамки.
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        # Создать элементы интерфейса для средней рамки.
        self.descr_label = tkinter.Label(self.mid_frame,
                   text='Преобразовано в мили:')

        # Объект StringVar нужен для того, чтобы его связать
        # с выходной надписью. Для сохранения последовательности 
        # пробелов используется метод set данного объекта.
        self.value = tkinter.StringVar()

        # Создать надпись Label и связать ее с объектом
        # StringVar. Любые значения, хранящиеся в 
        # объекте StringVar будут автоматически 
        # выводиться в надписи Label.
        self.miles_label = tkinter.Label(self.mid_frame,
                   textvariable=self.value)

        # Создать элементы интерфейса для средней рамки.
        self.descr_label.pack(side='left')
        self.miles_label.pack(side='left')

        # Создать элементы интерфейса Button для нижней рамки.
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text='Преобразовать',
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                   command=self.main_window.destroy)

        # Упаковать кнопки.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Упаковать рамки.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

    # Метод convert является функцией обратного вызова
    # для кнопки 'Преобразовать'.

    def convert(self):
        # Получить значение, введенное пользователем
        # в элемент интерфейса kilo_entry.
        kilo = float(self.kilo_entry.get())

        # Конвертировать километры в мили.
        miles = kilo * 0.6214

        # Конвертировать мили в символьную последовательность и 
        # сохранить ее в объекте StringVar. В результате элемент 
        # интерфейса miles_label будет автоматически обновлен.
        self.value.set(miles)

# Создать экземпляр класса KiloConverterGUI.
kilo_conv = KiloConverterGUI()