class Persona():
    __nombre=""
    apellido=""
    __edad=0
    genero="sin definir"

    def __init__(self, nombre, apellido, genero):
        self.__nombre=nombre
        self.apellido=apellido
        self.genero=genero

    def setEdad(self,edad):
        if edad<0 or edad>100:
            print ("introdujo una edad erronea")

        else:
            self.__edad=edad    
            return self.__edad      
    def hablar(self):

        return ("la persona que se llama " + self.nombre + " esta hablando" )

    def caminar(self):

        return(self.nombre + " esta caminando")
    
    def getdatos(self):

        return "Nombre: " + self.__nombre + " Apellido: " + self.apellido + \
            " Edad: "+ str(self.__edad) + " Genero: " + self.genero
    
P1=Persona("Santiago","fajardo","masculino ")

P1.setEdad(-7)

print(P1.getdatos())

P1.__nombre="david"
 
print(P1.getdatos())
