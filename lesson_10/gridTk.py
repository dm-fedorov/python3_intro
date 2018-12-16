import tkinter

root = tkinter.Tk()

for r in range(3):
   for c in range(4):
      tkinter.Label(root, text='Row{0}/Column{1}'.format(r, c), borderwidth=8).grid(row=r,column=c)

root.mainloop()
