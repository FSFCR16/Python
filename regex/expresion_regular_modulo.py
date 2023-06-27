#expresiones regulares
import re


# re.findall devulve una lista con todas las coincidencas que encontro, tambien puedes agregar un argumentoi de mas especificando el numero exacto de divisiones que quieres hacer
cadena="hello 12 hi 89. howdy 34"
pattern="\d+"

encontar=re.findall(pattern, cadena)
print(encontar)

#re.split

cadena1="the rain in spain"
x= re.split("\s", cadena1)
print(x)

cadena3="Doce:12 ochenta nueve:9."
z=re.split("\d+", cadena3,1)
print(z)


#El método devuelve una cadena donde las ocurrencias coincidentes se reemplazan con el contenido reemplazar variable.

frase="Santiago"
coincidencia="[a]"
replacee="h"

remplazar=re.sub(coincidencia,replacee,frase, 1)
print(remplazar) #si no se encuntra el patron re sub devuelve la cadena original

#es re.subn()similar a re.sub()excepto que devuelve una tupla de 2 elementos que contiene la nueva cadena y el número de sustituciones realizadas.
frase="Santiago"
coincidencia="[a]"
replacee="h"

remplazar=re.subn(coincidencia,replacee,frase)
print(remplazar)

#El re.search()método toma dos argumentos: un patrón y una cadena. El método busca la primera ubicación donde el patrón RegEx produce una coincidencia con la cadena. 
#Si la búsqueda tiene éxito, re.search()devuelve un objeto coincidente; si no, vuelve None.


strr="Santiago Fajardo esta estudiando programacion y estudiando para generar mas dinero"

match=re.search("estudiando", strr)
if match:
    print(match)

#El group()método devuelve la parte de la cadena donde hay una coincidencia.

numeros="Santiago Fajardo esta cominedo un omellete con Sandia"

pattern="\AS[^o]"

match=re.search(pattern, numeros)

if match:
    print(match.group())

else: 
    print("No fue encontrado")

