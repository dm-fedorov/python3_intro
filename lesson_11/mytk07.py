# mytk07.py
import tkinter

# Контроллер
def click():
    counter.set(counter.get() + 1)

if __name__ == '__main__':
    window = tkinter.Tk()
    # Модель
    counter = tkinter.IntVar()
    counter.set(0)
    # Вид
    frame = tkinter.Frame(window)
    frame.pack()

    button = tkinter.Button(frame, text='Click', command=click)
    button.pack()

    label = tkinter.Label(frame, textvariable=counter)
    label.pack()

    window.mainloop()
