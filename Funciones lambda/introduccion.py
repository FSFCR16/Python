#ejemplo de una funcion normal
"""def calcular_area_triangulo(base, altura):

    return (base*altura)/2

#ejemplo de una funcion lambda
area_triangulo=lambda base,altura:(base*altura)/2

print(area_triangulo(3,5))
 
#-------------------------------------------------

potencia_numeros=lambda numero, exponente:(numero**exponente)

print(potencia_numeros(5,6))

#-------------------------------------------------

comision_formato=lambda comision:"!{}¡$".format(comision)

comision1=input("")

print(comision_formato(comision1))

#-------------------------------------------------

mi_lista=[(5,11),(9,5),(26,2),(29,9)]

def ordena_lista(t):

    return t[0]+t[1]

mi_lista.sort(key=ordena_lista)
print(mi_lista)

#formato lambda

mi_lista1=[(5,11),(9,5),(26,2),(29,9)]
mi_lista1.sort(key=lambda tupla:tupla[0]+tupla[1])
print(mi_lista1)

#-------------------------------------------------


musicos=["Paul mcCartney", "Bruce Springteen", "Tina Turner", "Justin Biber", "Elton John"]


def odenar_apellidos(musico):

    return musico.split()[1]

musicos.sort(key=odenar_apellidos)

print(musicos)

#formato lambda

musicos2=["Paul mcCartney", "Bruce Springteen", "Tina Turner", "Justin Biber", "Elton John"]
musicos2.sort(key=lambda musicos:musicos.split()[1])
print(musicos2)"""


#Crea un programa de Python que muestre en consola las siguientes frases ordenadas de mayor a menor en función del número de palabras que forma cada frase, utilizando funciones lambda.

lista_frases=["Los lunes son los mejores días para programar","Python es moderno", "Veremos Inteligencia Artificial más adelante", "Lambda simplifica el código"]

def ordenar_frases(frase):
    
    return len(frase.split())

lista_frases.sort(reverse=True, key=ordenar_frases)
print(lista_frases)

#formato lambda
lista_frasess=["Los lunes son los mejores días para programar","Python es moderno", "Veremos Inteligencia Artificial más adelante", "Lambda simplifica el código"]
lista_frasess.sort(key=lambda frasee:len(frasee.split()), reverse=True)
print(lista_frasess)