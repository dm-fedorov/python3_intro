# Эта программа демонстрирует элемент интерфейса Button.
# Когда пользователь нажимает кнопку Button, 
# на экран выводится информационное диалоговое окно.

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

        # Упаковать элемент интерфейса Button.
        self.my_button.pack()

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