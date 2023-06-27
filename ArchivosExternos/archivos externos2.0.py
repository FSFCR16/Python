import os

import io

listaArchivos=os.listdir("./")

for archivo in listaArchivos:

    if archivo=="posts.csv":

        os.remove








"""os.makedirs("practicaDirectorio2")

os.chdir("practicaDirectorio2")

os.rename("arcvhivoExterno1.txt", "archivoEliminar.txt")

os.remove("arcvhivoExterno2.docx")
os.remove("arcvhivoExterno2.txt")
os.remove("arcvhivoExterno3.txt")

os.chdir("../")

os.rmdir("practicaDirectorio2")


print(os.getcwd())
print(os.listdir("./"))"""