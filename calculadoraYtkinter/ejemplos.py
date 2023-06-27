from tkinter import*
import tkinter.font as tkfont


raiz=Tk()

miframe=Frame(raiz)
miframe.pack()

for font in tkfont.families():

    print(font)
print()
print()
print(tkfont.names())
print()
print()
print(tkfont.nametofont("device"))

raiz.mainloop()