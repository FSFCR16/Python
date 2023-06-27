import re


"""nombres=["Santiago", "Fajardo", "Juan", "David", "Luis", "Guzman", "Samuel"]


for nombre in nombres:

    if re.findall("[^Fajardo]", nombre):

        print(nombre)   
print("-----------")

#-------------------------------------------------------------------------------

variables=["[", "/", "*"]

for variable in variables:

    if re.findall("\[", variable):

        print(variable)   
print("-----------")

#-------------------------------------------------------------------------------


lista_cadena=["a", "ac", "Hey Jude", "abc de ca"]

for palab in lista_cadena:

    if re.findall("^[abc]", palab):

        print(palab)


    else:

        print("palabra no encontrada")


print("-----------")

#-------------------------------------------------------------------------------


lista_nombres= ["Juan", "Luis", "Santiago", "David", "luan"]

for nombre in lista_nombres:

    if re.findall(".....ago", nombre):

        print(nombre)


print("-----------")

#-------------------------------------------------------------------------------


variable2= "abcbd"

variable3=re.findall("", variable2)

print(variable3)


print("-----------")


#-------------------------------------------------------------------------------

lista_prueba=["foo1", "nfoo2", "fooss"]


for palabra in lista_prueba:

    if re.findall("foo.$", palabra):

        print(palabra)


#-------------------------------------------------------------------------------

contador=0

lista_palabras=[]

while contador<5:

    palabra=input("escriba 5 en 10 segundos que empiecen por A y termines S: ")

    if re.match("^[as]$", palabra):

        lista_palabras.append(palabra)

    else:

        print("la palabra no empieza, ni termina por las letras asigndas")

    
    contador+=1


print(lista_palabras)

"""
#-------------------------------------------------------------------------

li=["ab123csde", "345673","12", "1"]

for pa in li:

    if re.findall("[0-9]{2,4}", pa):

        print(pa)


#-------------------------------------------------------------------------

li=["cde", "ade","acdbea"]

for pa in li:

    if re.findall("a|b ", pa):

        print(pa)

print("-----------")

#-------------------------------------------------------------------------

#Haga coincidir caulquier cadena que coincida con a, b o c seguido por xz

lista_cadenas =["ab xz", "abxz", "axz cabxz"]

for cadena in lista_cadenas:
    if re.findall("(a|b|c)xz", cadena):

        print(cadena)
