from tkinter import*

root=Tk()

miFrame=Frame(root, width=550, height=450)
miFrame.pack()


#miLabel=Label(miFrame, text="Mi primer interfaz grafica")
#miLabel.place(x=170, y=125)


miLogo=PhotoImage(file="descarga.png")

Label(miFrame,image=miLogo).place(x=100,y=125)

root.mainloop()