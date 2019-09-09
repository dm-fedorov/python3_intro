# Эта программа конвертирует расстояния в километрах
# в мили. Полученный результат выводится в
# информационном диалоговом окне.

import tkinter
import tkinter.messagebox

class KiloConverterGUI:
    def __init__(self):

        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать две рамки, чтобы сгруппировать элементы интер-фейса.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Создать элементы интерфейса для верхней рамки.
        self.prompt_label = tkinter.Label(self.top_frame,
                             text='Введите расстояние в километрах:')
        self.kilo_entry = tkinter.Entry(self.top_frame,
                                        width=10)

        # Упаковать элементы верхней рамки.
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

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

        # Показать результаты в информационном диалоговом окне.
        tkinter.messagebox.showinfo('Результаты',
                                    str(kilo) +
                                    ' километров эквивалентно ' +
                                    str(miles) + ' милям.')

# Создать экземпляр класса KiloConverterGUI.
kilo_conv = KiloConverterGUI()