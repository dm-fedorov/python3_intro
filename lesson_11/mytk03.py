# mytk03.py
import tkinter
window = tkinter.Tk()
data = tkinter.StringVar()
data.set('Данные в окне')

label = tkinter.Label(window, textvariable=data)
label.pack()

window.mainloop()
