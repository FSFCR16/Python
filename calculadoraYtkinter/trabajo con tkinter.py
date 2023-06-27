from tkinter import*

raiz=Tk()

raiz.title("Primera ventana python")

raiz.resizable(1,1)

raiz.iconbitmap("favicon (7).ico")

#raiz.geometry("700x400")

raiz.config(bg="white")

miFrame=Frame()

miFrame.pack(fill="y", expand=1)

miFrame.config(bg="black")

miFrame.config(width="560", height="350")

raiz.mainloop()