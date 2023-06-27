class Persona():
    
    def __init__(self, nombre, apellido, edad):
       
       self.nombre=nombre
       self.apelido=apellido
       self.edad=edad

    def getinfo(self):

        return ("El nombre es: " + self.nombre + " El apellido es: " + self.apelido + " Su edad es: " + str(self.edad))
    
    def habla(self):
        return ("Estoy hablando")
    
    def piensa(self):
        return ("Estoy pensando")
    
    def camina(self):
        return ("Estoy caminando")
    
    def come(self):
        return ("Estoy comiendo")
    
class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad,uni):
        Persona.__init__(self,nombre, apellido, edad)
        self.universidad=uni

    def estudia(self):
        return ("Estoy estudiando")
    
    def getinfo(self):
        return super().getinfo()+ " Universidad: "+ self.universidad

class Trabajador(Persona):
    def __init__(self, nombre, apellido, edad,empresa):
        Persona.__init__(self,nombre, apellido, edad)
        self.empresa=empresa

    def trabaja(self):
        return ("Estoy trabajando")
    
    def getinfo(self):
        return super().getinfo()+ " Empresa: "+ self.empresa


class Director(Trabajador, Estudiante):

    def __init__(self, nombre, apellido, edad, empresa, uni,bonus):
         
        Trabajador.__init__(self,nombre, apellido, edad, empresa)

        Estudiante.__init__(self,nombre, apellido, edad, uni)

        self.bonus=bonus

    def datosPersonales(self):
        return super().getinfo()+ " Bonus:" + str(self.bonus)
    
    def dirige(self):
        return "estoy dirigiendo"

persona1=Persona("Santiago", "Fajardo", 18)

estudiante1=Estudiante("Santiago", "Fajardo", 18, "EAN")

print(persona1.getinfo())
print(estudiante1.getinfo())
print("--------------------------------")

trabajador1=Trabajador("Gustavo","Ramirez",65,"Tesla")
print(trabajador1.getinfo())

director1=Director("David","Rass", 34,"Davivienda", "Ean", 2000000)
print(director1.datosPersonales())
