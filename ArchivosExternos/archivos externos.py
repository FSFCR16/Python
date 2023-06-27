from io import open


archivo_externo=open("arcvhivoExterno.txt",mode="r+")

lectura=archivo_externo.readlines()

lectura[1]="5 ideas de empredimientos \n"

archivo_externo.seek(0)

antes=archivo_externo.writelines(lectura)

archivo_externo.close()

