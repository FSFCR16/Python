from tkinter import *

from calculadora.Posicionamiento_Botones import *

import re

raiz=Tk()

class Calculadora:

    def __init__(self, ventana):

        self.ventana=ventana
        self.ventana.title("Calculadora POO")
        self.operacion=""

        #Display

        self.pantalla=Entry(ventana, font="Arial 20")
        
        #Ubicar display

        self.pantalla.grid(row=1, column=0, columnspan=4, pady=10)

        #formato display

        self.pantalla.config(background="black", fg="#04FC0C", justify="right", width=20)
        
        #creacion de botones

        boton7=colocar_boton(self,7)
        boton8=colocar_boton(self, 8)
        boton9=colocar_boton(self,9)
        botonDiv=colocar_boton(self,"/")
        botonDiv.config(text="÷")
        #--------------------------------------------------
        boton4=colocar_boton(self,4)
        boton5=colocar_boton(self,5)
        boton6=colocar_boton(self,6)
        botonMul=colocar_boton(self,u"\u00D7")
        #botonMul.config(text="x")
        #--------------------------------------------------
        boton3=colocar_boton(self,3)
        boton2=colocar_boton(self,2)
        boton1=colocar_boton(self,1)
        botonRes=colocar_boton(self,"-")

        #--------------------------------------------------
        boton0=colocar_boton(self,0)
        botonComa=colocar_boton(self,".")
        botonIgual=colocar_boton(self,"=", mostrar=False)
        botonSuma=colocar_boton(self,"+")

        #--------------------------------------------------

        botones=[boton7, boton8, boton9, botonDiv, boton4, boton5, boton6, botonMul, boton3, boton2, boton1, botonRes, boton0, botonComa, botonIgual, botonSuma]
        
        posiscionBotones(self, botones, 4)

mi_calculadora=Calculadora(raiz)

raiz.mainloop() 
