from tkinter import *
from tkinter import messagebox as MessageBox

raiz=Tk()

miFrame=Frame(raiz, width=1000, height=500)
miFrame.pack()



miVariable=StringVar()

#nombre
cuadroNom=Entry(miFrame, textvariable=miVariable)
cuadroNom.grid(row=0,column=1, padx=15, pady=10)

nombre=Label(miFrame, text="Nombre:")
nombre.grid(row=0,column=0, sticky="e")

#apellido
cuadroApe=Entry(miFrame)
cuadroApe.grid(row=1,column=1, padx=15, pady=10)

apellido=Label(miFrame, text="apellido:")
apellido.grid(row=1,column=0,sticky="e")

#contraseña
cuadroTextocontra=Entry(miFrame)
cuadroTextocontra.grid(row=2,column=1, padx=15, pady=10)
cuadroTextocontra.config(show="*")

contraseña=Label(miFrame, text="contraseña:")
contraseña.grid(row=2,column=0,sticky="e")

#direccion
cuadrodire=Entry(miFrame)
cuadrodire.grid(row=3,column=1, padx=15, pady=10)

direccion=Label(miFrame, text="direccion de hogar:")
direccion.grid(row=3,column=0,sticky="e")

#correo
cuadroTexto=Entry(miFrame)
cuadroTexto.grid(row=4,column=1, padx=15, pady=10)

correo=Label(miFrame, text="correo:")
correo.grid(row=4,column=0,sticky="e")

#comentarios

cuadroTextocomen=Text(miFrame, width=15, height= 5)
cuadroTextocomen.grid(row=5, column=1, padx=15, pady=10)

 
correo=Label(miFrame, text="comentarios:")
correo.grid(row=5,column=0,sticky="e")



#barra
barra=Scrollbar(miFrame, command=cuadroTextocomen.yview)
barra.grid(row=5,column=2, sticky="nsew")

cuadroTextocomen.config(yscrollcommand=barra.set)


#button
def funcionBoton():


    miVariable.set("Santiago")
    #datospersonas= f"Nombre: {cuadroNom.get()} \n Apellido: {cuadroApe.get()} \n Contraseña: {cuadroTextocontra.get()} \n Direccion: {cuadrodire.get()} \n Correo: {cuadroTexto.get()} "

    #MessageBox.showinfo("Datos de la perosna", )
    
    

botonEnviar=Button(raiz, text="Enviar", command=funcionBoton)
botonEnviar.pack()



raiz.mainloop()