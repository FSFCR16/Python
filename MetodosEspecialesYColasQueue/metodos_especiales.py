class Persona():


    def __init__(self, **dat):


        elementos=dat.items()

        for clave,valor in elementos:
            print(clave, "=", valor)


p1=Persona(nombre="Santiago", apellido="Fajardo", edad=14, salario=350000 )

print(p1)