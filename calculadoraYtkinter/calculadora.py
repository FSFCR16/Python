from tkinter import *

import tkinter.font as tkFont

raiz=Tk()

miFrame=Frame(raiz)

miFrame.pack()

operacion=""

resultado=0

digitodisplay=StringVar()

coma=False

#---------------Display----------------


pantalla=Entry(miFrame, textvariable=digitodisplay, font="Arial 20")
pantalla.grid(row=1, column=1, columnspan=4, pady=10 )
pantalla.config(background="black", fg="#04FC0C", justify="right", width=20)
digitodisplay.set("0")


#--------------funciones teclas-----------

def pulsacionesteclas(numPulsado):

    global operacion 

    global coma 
    
    if operacion!="":

        digitodisplay.set(numPulsado)

        operacion=""

    else: 

        if numPulsado=="0" and digitodisplay.get()=="0":
            digitodisplay.set("0")

        elif numPulsado!=0 and digitodisplay.get()=="0":
            digitodisplay.set(numPulsado)
        else:
            digitodisplay.set(digitodisplay.get()+ numPulsado)

#-------------------tecla coma------------------
def pulsaciomComa():
    
    global coma 

    for caracter in digitodisplay.get():

        if caracter==".":

            coma=True

    if coma==False:

        digitodisplay.set(digitodisplay.get()+ ".")

#------------------tecla suma---------------
def suma(num):


    global operacion 

    global resultado

    resultado+=float(num)

    if resultado.is_integer():

        digitodisplay.set(int(resultado))
    
        operacion="suma"


    else:

        operacion="suma"

        digitodisplay.set(resultado)


#-------------funcion total------------------

def total(num):
    
    global resultado

    if (resultado+float(digitodisplay.get())).is_integer():
        
        digitodisplay.set(int(resultado+float(digitodisplay.get())))
        
        resultado=0


    else:
        digitodisplay.set(resultado+float(digitodisplay.get()))

        resultado=0

#-------------Primer Fila--------------

boton7=Button(miFrame, text="7", width=10, height=2, command=lambda:pulsacionesteclas("7"))
boton7.grid(row=2, column=1)

boton8=Button(miFrame, text="8", width=10, height=2, command=lambda:pulsacionesteclas("8"))
boton8.grid(row=2, column=2)

boton9=Button(miFrame, text="9", width=10, height=2, command=lambda:pulsacionesteclas("9"))
boton9.grid(row=2, column=3)

botonDiv=Button(miFrame, text="÷", width=10, height=2, command=lambda:pulsacionesteclas("÷"))
botonDiv.grid(row=2, column=4)

#-------------Segunda Fila--------------

boton4=Button(miFrame, text="4", width=10, height=2, command=lambda:pulsacionesteclas("4"))
boton4.grid(row=3, column=1)

boton5=Button(miFrame, text="5", width=10, height=2, command=lambda:pulsacionesteclas("5"))
boton5.grid(row=3, column=2)

boton6=Button(miFrame, text="6", width=10, height=2, command=lambda:pulsacionesteclas("6"))
boton6.grid(row=3, column=3)

botonMul=Button(miFrame, text="x", width=10, height=2, command=lambda:pulsacionesteclas("x"))
botonMul.grid(row=3, column=4)

#-------------Tercera Fila--------------

boton1=Button(miFrame, text="1", width=10, height=2, command=lambda:pulsacionesteclas("1"))
boton1.grid(row=4, column=1)

boton2=Button(miFrame, text="2", width=10, height=2, command=lambda:pulsacionesteclas("2"))
boton2.grid(row=4, column=2)

boton3=Button(miFrame, text="3", width=10, height=2, command=lambda:pulsacionesteclas("3"))
boton3.grid(row=4, column=3)

botonMen=Button(miFrame, text="-", width=10, height=2)
botonMen.grid(row=4, column=4)

#-------------Cuarta Fila--------------

boton0=Button(miFrame, text="0", width=10, height=2, command=lambda:pulsacionesteclas("0"))
boton0.grid(row=5, column=1)

botoncoma=Button(miFrame, text=".", width=10, height=2,command=lambda:pulsaciomComa())
botoncoma.grid(row=5, column=2)

botonigual=Button(miFrame, text="=", width=10, height=2,command=lambda:suma(digitodisplay.get()))
botonigual.grid(row=5, column=3)

botonsum=Button(miFrame, text="+", width=10, height=2, command=lambda:suma(digitodisplay.get()))
botonsum.grid(row=5, column=4)


raiz.mainloop()