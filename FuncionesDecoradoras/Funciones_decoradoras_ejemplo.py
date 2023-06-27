def funcion_decoradora(funcionB):

    def funcion_interna():
        

        print("A continuacion voy a realizar un calculo")

        funcionB()

        print("ya he termindao el trabajo")

    return funcion_interna




@funcion_decoradora
def suma():

    print(23+35)


 
def resta():
    print(80-35)

suma()