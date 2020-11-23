import Menus
import Matrices
print("*+*+*+*Bienvenido a MI Calculadora De MATRICES*+*+*+*")
n = Menus.IngresoNumeroValido("Por favor ingrese el numero de matrices que quiere almacenar en la memoria:", "Error!!!! El valor ingresado es incorrecto")
MemoriaMatrices = [[]]*n
while (opcion:=Menus.MenuPrincipal())!="4"  :
    if opcion=="1":
        while (opcion1:=Menus.IngresarMatrices())!="3":
            if opcion1=="1":
                print("Acciones para ingresar matriz en posicion inicial o existente")
                Menus.crearMatriz(MemoriaMatrices)
            elif opcion1=="2":
                print("Acciones para ingresar matriz en posicion libre")
                Menus.crearMatriz(MemoriaMatrices)
    elif opcion=="2":
       while(opcion:=Menus.operarMatrices())!="5":
           if opcion=="1":
               print("Colocamos la función que suma matrices")
               a1 = Menus.IngresoNumeroValido("Elige la primera matriz que desea sumar: ", "Error!!!! El valor ingresado es incorrecto")
               a2 = Menus.IngresoNumeroValido("Elige la segunda matriz que desea sumar: ", "Error!!!! El valor ingresado es incorrecto")
               b1=a1-1
               b2=a2-1
               if b1 < n:
                   matriz1=MemoriaMatrices[b1]
                   print("Este es la primera matriz",matriz1)
               else:
                   print("Querido Usuario!!! La matriz que ingreso no existe!!!!!")

               if b2 < n:
                   matriz2=MemoriaMatrices[b2]
                   print("Este es la segunda matriz",matriz2)
               else:
                   print("Querido Usuario!!! La matriz que ingreso no existe!!!!!")
               if len(matriz1)==len(matriz2)and len(matriz1[0])==len(matriz2[0]):
                       print(Matrices.sumamatriz(matriz1, matriz2))
               else:
                    print("Alerta!!!!! Querido usuario recuerde que las matrices deben de ser m*n")

           elif opcion=="2":
               print("La función que resta matrices")
               a1 = Menus.IngresoNumeroValido("Elige la primera matriz que desea restar: ", "Error!!!! El valor ingresado es incorrecto")
               a2 = Menus.IngresoNumeroValido("Elige la segunda matriz que desea restar: ", "Error!!!! El valor ingresado es incorrecto")
               b1= a1-1
               b2= a2-1
               if b1 < n:
                   matriz1=MemoriaMatrices[b1]
                   print("Este es la primera matriz",matriz1)
               else:
                   print("Querido Usuario!!! La matriz que ingreso no existe!!!!!")

               if b2 < n:
                   matriz2=MemoriaMatrices[b2]
                   print("Este es la segunda matriz",matriz2)
               else:
                   print("Querido Usuario!!! La matriz que ingreso no existe!!!!!")
               if len(matriz1)==len(matriz2)and len(matriz1[0])==len(matriz2[0]):
                       print(Matrices.restamatriz(matriz1, matriz2))
               else:
                    print("Alerta!!!!! Querido usuario recuerde que las matrices deben de ser m*n")

           elif opcion=="3":
                print("Función que multiplica matrices")
                a1 =Menus.IngresoNumeroValido("Elige la primera matriz que desea multiplicar: ","Error!!!! El valor ingresado es incorrecto")
                a2 =Menus.IngresoNumeroValido("Elige la segunda matriz que desea multiplicar: ","Error!!!! El valor ingresado es incorrecto")
                b1= a1 -1
                b2= a2 -1
                if b1 < n:
                    matriz1 = MemoriaMatrices[b1]
                    print("Este es la primera matriz: ", matriz1)
                else:
                    print("Querido Usuario!!! La matriz que ingreso no existe!!!!!")

                if b2 < n:
                    matriz2 = MemoriaMatrices[b2]
                    print("Este es la segunda matriz: ", matriz2)
                else:
                    print("Querido Usuario!!! La matriz que ingreso no existe!!!!!")

                if len(matriz1[0])==len(matriz2):
                    print(Matrices.multiplicacion(matriz1, matriz2))
                else:
                    print("Alerta!!!!! Querido usuario recuerde que las matrices deben de ser m*n y n*p")

           elif opcion=="4":
                print("Función que traspone una matriz")
                a=Menus.IngresoNumeroValido("Elige la matriz que desea trasponer: ", "Error!!!! El valor ingresado es incorrecto")
                b=a-1
                if b<n:
                    Matriz3=MemoriaMatrices[b]
                    print("Matriz a trasponer: ",Matriz3)
                    matriztraz=Matrices.trasponerMatrices(Matriz3)
                    print(matriztraz)
                else:
                    print("La matriz no existe en la memoria")

    elif opcion=="3":
        while(opcion:=Menus.MostrarMatrices())!="3":

            if opcion=="1":
                print("LISTADO DE MATRICES ",MemoriaMatrices)
            elif opcion=="2":

                a = Menus.IngresoNumeroValido("Ingrese el orden de la matriz que desea ver en la memoria: ", "Error!!!! El valor ingresado es incorrecto")
                b = a-1
                if b<n:
                    print(MemoriaMatrices[b])
                else:
                    print("La matriz no existe en la memoria")

print("++++****++++ Gracias usar nuestra CaLcUlAdOrA de MaTrIcEs ++++****++++")
