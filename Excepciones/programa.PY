def nombre_repetidos():
    contador=0
    list_nom=[]
    while contador!=10:  
        nombre=input("Digite el nombre:")
        
        if nombre in list_nom:
                
            raise ValueError("Error.ese nombre ya fue introducido")

        else:

            list_nom.append(nombre)
    
        contador+=1

nombre_repetidos()




        
