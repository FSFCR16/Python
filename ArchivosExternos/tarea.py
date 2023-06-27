from io import open


archivo_externo=open("arcvhivoExterno.txt",mode="a")

archivo_externo.write("\n montar un babershop pero tambien peluqueria en panama ")

"""archivo=archivo_externo.readlines()

for row in archivo:

    for palabra in row.split(" "):

        if palabra=="externos":

            print (row)"""

archivo_externo.close()