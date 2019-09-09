# Эта программа демонстрирует группу элементов Radiobutton.
import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать две рамки. Одну для элементов Radiobutton
        # и еще одну для обычных элементов Button.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
 
        # Создать объект IntVar для использования с
        # элементами Radiobutton.
        self.radio_var = tkinter.IntVar()
 
        # Назначить объекту IntVar значение 1.
        self.radio_var.set(1)

        # Создать элементы Radiobutton в рамке top_frame.
        self.rb1 = tkinter.Radiobutton(self.top_frame,
                                       text='Вариант 1',
                                       variable=self.radio_var,
                                       value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame,
                                       text='Вариант 2',
                                       variable=self.radio_var,
                                       value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame,
                                       text='Вариант 3',
                                       variable=self.radio_var,
                                       value=3)

        # Упаковать элементы Radiobutton.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Создать кнопку 'OK' и кнопку 'Выйти'.
        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text='OK',
                                        command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                command=self.main_window.destroy)

        # Упаковать элементы Button.
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Упаковать рамки.
        self.top_frame.pack()
        self.bottom_frame.pack()
 
        # Запустить главный цикл.
        tkinter.mainloop()

    # Метод show_choice является функцией обратного вызова
    # для кнопки OK.
    def show_choice(self):
        tkinter.messagebox.showinfo('Выбор', 'Выбран вариант ' +
                                    str(self.radio_var.get()))

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()