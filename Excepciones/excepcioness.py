def nombre_repetidos():

    list_nom=[]
    for i in range(0,10):

        nombre=input("Digite el nombre:")
        try:
            if nombre in list_nom:
                
                raise ValueError 
            
        
            
        except ValueError:
            
            print("Error.ese nombre ya fue introducido", nombre)
            
        else:
            list_nom.append(nombre)
        
    print(list_nom)
        

nombre_repetidos()
