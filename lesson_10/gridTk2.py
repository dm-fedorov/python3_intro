from  tkinter import *
root = Tk()
count = 0

b = 0

for r in range(6):
   for c in range(6):
      b += 1
      Button(root, text=str(b), borderwidth=3).grid(row=r,column=c)

root.mainloop()
