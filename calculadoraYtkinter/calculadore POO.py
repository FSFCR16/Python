from tkinter import *
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

        boton7=self.colocar_boton(7)
        boton8=self.colocar_boton(8)
        boton9=self.colocar_boton(9)
        botonDiv=self.colocar_boton("/")
        botonDiv.config(text="÷")
        #--------------------------------------------------
        boton4=self.colocar_boton(4)
        boton5=self.colocar_boton(5)
        boton6=self.colocar_boton(6)
        botonMul=self.colocar_boton(u"\u00D7")
        #botonMul.config(text="x")
        #--------------------------------------------------
        boton3=self.colocar_boton(3)
        boton2=self.colocar_boton(2)
        boton1=self.colocar_boton(1)
        botonRes=self.colocar_boton("-")

        #--------------------------------------------------
        boton0=self.colocar_boton(0)
        botonComa=self.colocar_boton(".")
        botonIgual=self.colocar_boton("=", mostrar=False)
        botonSuma=self.colocar_boton("+")

        #--------------------------------------------------

        botones=[boton7, boton8, boton9, botonDiv, boton4, boton5, boton6, botonMul, boton3, boton2, boton1, botonRes, boton0, botonComa, botonIgual, botonSuma]

        contador=0

        for fila in range(2,6):

            for columna in range(4):

                botones[contador].grid(row=fila, column=columna)

                contador+=1

    def colocar_boton(self, valor, mostrar=True, ancho=10, alto=2):

        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica", 9), 
        command=lambda:self.pulsacionesTeclas(valor, mostrar))
    
    def pulsacionesTeclas(self, valor, mostrar):
        
        if mostrar:
            

            self.operacion+=str(valor)

            self.mostrar_pantalla(valor)

        elif not mostrar and valor=="=":
            
            self.operacion=re.sub(u"\u00D7","*", self.operacion)
            
            self.borrar_pantalla()

            self.mostrar_pantalla(str(eval(self.operacion)))

        else:

            pass

    def mostrar_pantalla(self, valor):
        
        self.pantalla.insert(END, valor)

    def borrar_pantalla(self):

        self.pantalla.delete(0,END)


mi_calculadora=Calculadora(raiz)



raiz.mainloop()
