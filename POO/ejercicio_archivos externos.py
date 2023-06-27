import os
import io
import csv
os.chdir(r"c:\Users\INTEL\Downloads")

os.chdir("clientes")
 
archivo_externo=open("clientes.txt",mode="r",encoding="UTF-8") 

archivo=archivo_externo.readlines()

archivo_externo.close()

clientes=[]

for row in archivo:

    campos=row.split(";")

    cliente={"codigo":campos[0],"Nombre":campos[1], "Direcccion":campos[2], "Poblacion":campos[3], "Telefono":campos[4], "Responsable":campos[5]}


    clientes.append(cliente)

    for c in clientes:

        print("Codigo Articul={} Nombre={} Direcccion={} Poblacion={} Telefono={} Responsable={}".format(c["codigo"],c["Nombre"],c["Direcccion"],c["Poblacion"],c["Telefono"],c["Responsable"]))


    
























"""contador2=0
while contador2!=35:
    listacar=[]
    
    contador=0
    for clientes in archivo:
        contador2+=1

        for caracteristicas in clientes.split(";"):

            if contador!=6:
                listacar.append(caracteristicas)
                contador+=1
                

                if "\n" in listacar:

                    listacar.pop()
                    contador-=1
                    
                    
            else:
                cl=cliente(listacar[0],listacar[1],listacar[2],listacar[3],listacar[4],listacar[5])
                print(cl.clientes())
                listacar.clear()
                contador=0"""

"""class cliente:

    def __init__(self,codigo_articulo,nombre,direccion,poblacion,Tfon,responsable) :

        self.codigo_articulo=codigo_articulo
        self.nombre=nombre
        self.direccion=direccion
        self.poblacion=poblacion
        self.Tfon=Tfon
        self.responsable=responsable

    
class infoClientes:

    def clientes(self):
        
        archivo_externo=open("clientes.txt",mode="r",encoding="UTF-8") 

        archivo=archivo_externo.readlines()


        for row in archivo:

            for caracteristica in row.split(";"):

                if caracteristica==row[0]:

                    codigo_articulo=caracteristica

                if caracteristica==row[1]:

                    nombre=caracteristica
                if caracteristica==row[2]:

                    direccion=caracteristica
                if caracteristica==row[3]:

                    poblacion=caracteristica
                if caracteristica==row[4]:

                    Tfon=caracteristica
                if caracteristica==row[5]:

                    responsable=caracteristica
                

                yield cliente(codigo_articulo,nombre,direccion,poblacion,Tfon,responsable)

                
        
            return "Codigo Articulo="+ codigo_articulo,"Nombre="+nombre,"Direcion="+direccion,"Poblacion="+poblacion,"Tfon="+Tfon,"Responsable="+ responsable

cl=infoClientes()"""


