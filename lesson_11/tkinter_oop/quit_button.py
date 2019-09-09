# Эта программа содержит кнопку 'Выйти', которая
# при ее нажатии вызывает метод destroy класса Tk .

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Создать элемент интерфейса главного окна.
        self.main_window = tkinter.Tk()

        # Создать элемент интерфейса Button widget.
        # На кнопке должен появиться текст 'Нажми меня!'.
        # Когда пользователь нажимает кнопку,
        # должен быть исполнен метод do_something.
        self.my_button = tkinter.Button(self.main_window,
                                        text='Нажми меня!',
                                command=self.do_something)

        # Создать кнопку 'Выйти'. При нажатии этой кнопки вызыва-ется
        # метод destroy корневого элемента интерфейса (переменная
        # main_window ссылается на корневой элемент, поэтому функцией
        # обратного вызова является self.main_window.destroy.)
        self.quit_button = tkinter.Button(self.main_window,
                                          text='Выйти',
                                command=self.main_window.destroy)


        # Упаковать элементы интерфейса Button.
        self.my_button.pack()
        self.quit_button.pack()

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

    # Метод do_something является функцией обратного
    # вызова для элемента интерфейса Button.

    def do_something(self):
        # Показать информационное диалоговое окно.
        tkinter.messagebox.showinfo('Реакция',
                                     'Благодарю, что нажали кнопку.')

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()