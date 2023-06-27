def contraseña(contraseña):
    listamayus=[]
    listaespacios=[]

    while len(contraseña) < 10 or contraseña.isalnum()==True or contraseña.isupper()==False and contraseña.isspace()==False:

        if len(contraseña) < 10:
            print("El usuario no puede tener menos de 10 caracteres")
            new=input("Ingrese otra contraseña: ")
            contraseña=new

        if contraseña.isalnum()==True:
            print("La contraseña debe contener un carácter que no sea ni letra ni número")
            new=input("Ingrese otra contraseña: ")
            contraseña=new

        if contraseña.isupper()==False: 
            for letra in contraseña:
                if letra.isupper()==True:
                    listamayus.append(letra)
            s=''.join(listamayus)

            if s.isupper()==True:
                contraseña.isupper()==True
                
            else:
                print("la contraseña no es segura")    
                new=input("Ingrese otra contraseña: ")
                contraseña=new


        if contraseña.isspace()==False: 
            for letra in contraseña:
                if letra.isspace()==False:
                    listaespacios.append(letra)

                else:
                    print("la contraseña no puede contener espacios")    
                    new=input("Ingrese otra contraseña: ")
                    contraseña=new

