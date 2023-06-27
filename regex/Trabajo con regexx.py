import re 

lista_terminos=["camion", "camión", "niños", "niñas", "ejemplos"]

for nombre in lista_terminos:

    if re.findall("[l-r]$", nombre):

        print(nombre)

