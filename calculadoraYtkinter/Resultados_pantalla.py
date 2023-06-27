from tkinter import * 

def mostrar_pantalla(self, valor):
        
    self.pantalla.insert(END, valor)

def borrar_pantalla(self):

    self.pantalla.delete(0,END)