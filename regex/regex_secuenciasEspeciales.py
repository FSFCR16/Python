import re

#\A coincide si los caracteres especificados estan al principio de una cadena

lista_nueva=["the sun", " in the sun"]
for cadena in lista_nueva:
    if re.findall("\Athe", cadena):
        print(cadena)
print("-------------------------")
#\b Coincide si los carecteres especificados estan especificados al principio o al final de una palabra

lista_caracteres_PF=["football","a football","afootball","the foo", "the afoo test","the afootest", ]
for carac in lista_caracteres_PF:
    if re.findall(r"foo\b", carac):
        print(carac)

lista_caracteres_PF=["football","a football","afootball","the foo", "the afoo test","the afootest", ]
for carac in lista_caracteres_PF:
    if re.findall(r"\bfoo", carac):
        print(carac)

print("-------------------------")
#\B Es lo opuesto a \b

lista_caracteres_PF=["football","a football","afootball","the foo", "the afoo test","the afootest", ]
for carac in lista_caracteres_PF:
    if re.findall(r"foo\B", carac):
        print(carac)

lista_caracteres_PF=["football","a football","afootball","the foo", "the afoo test","the afootest"]
for carac in lista_caracteres_PF:
    if re.findall(r"\Bfoo", carac):
        print(carac)

alafanumericos=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A","B", "C", "D",
                "E", "F","G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Coincide con cualquier carácter alfanumérico (dígitos y alfabetos). equivalente a [a-zA-Z0-9_]. Por cierto, el guión bajo _también se considera un carácter alfanumérico
for caracter in alafanumericos:

    if re.findall("[\w]", caracter):

        print(caracter)   # Esto es igual a : [a-zA-Z0-9_]
print("-----------")


#Coincide con cualquier dígito decimal. Equivalente a[0-9]

alafanumericos=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A","B", "C", "D",
                "E", "F","G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                "S", "T", "U", "V", "W", "X", "Y", "Z"]


for caracter in alafanumericos:

    if re.findall("[\d]", caracter):

        print(caracter)   # Esto es igual a : [0-9]
print("-----------")

#Coincide con cualquier dígito no decimal. Equivalente a[^0-9]

alafanumericos=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A","B", "C", "D",
                "E", "F","G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                "S", "T", "U", "V", "W", "X", "Y", "Z"]


for caracter in alafanumericos:

    if re.findall("[\D]", caracter):

        print(caracter)    # Esto es igual a : [^0-9]
print("-----------")

#Coincide donde una cadena contiene cualquier carácter de espacio en blanco. equivalente a [ \t\n\r\f\v]

variable="Hola soy Santiago Fajardo Sabogal"

for string in variable:

    if re.findall("[\s]", string):

        print(string)   # Esto es igual a : [\t\n\r\f\v]
print("-----------")

#Coincidencias donde una cadena contiene cualquier carácter que no sea un espacio en blanco. equivalente a [^ \t\n\r\f\v]

variable="Hola soy Santiago Fajardo Sabogal"

for string in variable:

    if re.findall("[\S]", string):

        print(string)   # Esto es igual a : [^ \t\n\r\f\v]
print("-----------")

# Coincide con cualquier carácter no alfanumérico. Equivalente a[^a-zA-Z0-9_]

alafanumericos=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A","B", "C", "D",
                "E", "F","G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                "S", "T", "U", "V", "W", "X", "Y", "Z","*"]


for caracter in alafanumericos:

    if re.findall("[\W]", caracter):

        print(caracter)   # Esto es igual a : [^a-zA-Z0-9_]
print("-----------")

#-------------------------------------------------------------------------------

alafanumericos=["0,", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A","B", "C", "D",
                "E", "F","G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                "S", "T", "U", "V", "W", "X", "Y", "Z","*"]


for caracter in alafanumericos:

    if re.findall("[\s,]", caracter):

        print(caracter)   # Esto es igual a : [^a-zA-Z0-9_]
print("-----------")

#Coincide si los caracteres especificados están al final de una cadena

lista_can=["I like Python", "I like Python Programming", "Python is fun"]

for i in lista_can:
    if re.findall("Python\Z",i):
        print(i)

#-----------------------------------------------------------------------------
txt = "8 times before 11:45 AM"

#Check if the string has any two-digit numbers, from 00 to 59:

x = re.findall("[0-5][0-9]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")