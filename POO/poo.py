class Carro():

    #propiedades

    ruedas=4

    largoChasis=260

    anchoChasis=130

    arrancado=False

    #metodo

    def arrancar(self):

        self.arrancado=True
    
    def estadoCoche(self):
        if(self.arrancar):
            return "el coche esta arrancado"
        else:
            return "el coche esta parado"

mazda=Carro() #ejemplecar de clase

mercedes=Carro() #segundo ejemplar

print("el carro mazda tiene " + str(mazda.ruedas) + " ruedas")

mazda.arrancar()

print(mazda.estadoCoche())