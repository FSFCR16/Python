def usuario(usuario):
    while len(usuario) < 5 or len(usuario) > 15 or usuario.isalnum()==False: 
        if len(usuario) < 5:
            print("El usuario no puede tener menos de 5 caracteres")  
            new=input("Ingrese un usuario: ")
            usuario=new

        if len(usuario) > 15:
            print("El usuario no puede tener menos de 15 caracteres")
            if len(usuario) > 15:   
                new=input("Ingrese un usuario: ")
                usuario=new


        if usuario.isalnum()==False:
                print("El usuario solo puede tener numeros o letras")
                if usuario.isalnum()==False:
                    new=input("Ingrese un usuario: ")
                    usuario=new
                return(True)




        
    