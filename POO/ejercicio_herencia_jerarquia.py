class Vehiculo():
    def __init__(self, color, ruedas, ancho, alto, asientos):

        self.color=color
        self.ruedas=ruedas
        self.ancho=ancho
        self.alto=alto
        self.asientos=asientos

    def arrancar(self):
        return "Puede arrancar arrancado"
    def acelerar(self):
        return "Puede acelelar"
    def frenar(self):
        return "Puede frenar"
    def girar(self):
        return "Puede girar"
    def getInfo(self):
        return ("\nColor del vehiculo: "+ self.color + " \nNumero de ruedas: "+ str(self.ruedas)+" \nAncho del vehiculo: "+ str(self.ancho)+ "cm2" + " \nAlto del vehiculo: "+ str(self.alto)+ "cm"  " \nNumero de asisemtos: "+str(self.asientos))

class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, ancho, alto, asientos):
        super().__init__(color, ruedas, ancho, alto, asientos)

    def saltar(self):
        return("Puede saltar")
    
    def getInfo(self):
        return super().getInfo()
    
class Moto(Vehiculo):
    def __init__(self, color, ruedas, ancho, alto, asientos, Velocidades, cilindraje):
        super().__init__(color, ruedas, ancho, alto, asientos)

        self.cilindraje=cilindraje
        self.velocidades=Velocidades

    def derrapar(self):
        return "Puede derrapar"
    
    def getInfo(self):
        return super().getInfo() + " \nCantidad de velocidades: "+ str(self.velocidades)+ " \nCilindraje de la moto: " + str(self.cilindraje)
    
class Coche(Moto):

    def __init__(self, color, ruedas, ancho, alto, asientos, Velocidades, cilindraje,aire_acondicionado):
        super().__init__(color, ruedas, ancho, alto, asientos, Velocidades, cilindraje)
        
        self.aire_acondicionado=aire_acondicionado
        
    def irMarchaTras(self):
        return "Puede dar marcha atras"
    
    def getInfo(self):
        return super().getInfo() + " \nNivel del aire acondicionado: "+ str(self.aire_acondicionado)
    
class Furgoneta(Coche):

    def __init__(self, color, ruedas, ancho, alto, asientos, Velocidades, cilindraje, aire_acondicionado,carga):
        super().__init__(color, ruedas, ancho, alto, asientos, Velocidades, cilindraje, aire_acondicionado)

        self.carga=carga

    def cargar(self):
        return "Puede cargar"
    
    def getInfo(self):
        return super().getInfo()+ " \nEste vehiculo puede cargar: " + str(self.carga)+ "kg"


BMX=Bicicleta("Negra", 2, 75, 163,1)
Ducati=Moto("Roja",2,209,83,2,6,1200)
Mercedes=Coche("Gris",4,400,180,5,6,2000,2)
Furgon=Furgoneta("Blanca",4,530,190,8,5,3000,0,300)
    
print("BMX: "+BMX.getInfo())
print("------------------------------------------")
print("Ducati: "+Ducati.getInfo())
print("------------------------------------------")
print("Mercedes: "+Mercedes.getInfo())
print("------------------------------------------")
print("Furgoneta: "+Furgon.getInfo())
print("------------------------------------------")