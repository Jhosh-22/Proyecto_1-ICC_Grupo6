def MenuPrincipal():
    while True:
        print("MENU PRINCIPAL")
        print("[1] Ingresar Matrices")
        print("[2] Operar Matrices")
        print("[3] Mostrar Matrices")
        print("[4] Salir")
        opcion = input("Seleccione opción: ")
        if opcion in ["1","2","3","4"]:
            return opcion
        else:
            print("Opción no válida!!! Vuelva a intentarlo")
    

def IngresarMatrices():
    while True:
        print("MENU 1")
        print("[1] Ingresar una Matriz a una de memoria de matriz especificada ")
        print("[2] Ingresar una matriz a una memoria libre")
        print("[3] Salir")
        opcion = input("Seleccione opción: ")
        if opcion in ["1","2","3"]:
            return opcion
        else:
            print("Opción no válida!!! Vuelva a intentarlo")
    

def crearMatriz(MM):

    m = IngresoNumeroValido("Filas: ", "Error!!!! El valor ingresado es incorrecto")
    n = IngresoNumeroValido("Columnas: ", "Error!!!! El valor ingresado es incorrecto")
    matriz = [[0]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            matriz[i][j] =IngresoNumeroValido(f"M[{i}][{j}] = ","El valor ingreso no es permitido")
    posi = IngresoNumeroValido("Ingrese posicion de matriz: ","Posicion no permitida" )
    pos = posi-1
    MM[int(pos)] = matriz

def operarMatrices ():
    while True:
        print("Operar matrices")
        print("[1] Suma de matrices")
        print("[2] Resta de matrices")
        print("[3] Multiplicacion de matrices")
        print("[4] Trasposición de matriz")
        print("[5] Salir")
        opcion = input("Seleccione opción: ")
        if opcion in ["1", "2", "3", "4", "5"]:
            return opcion
        else:
            print("Opción no válida!!! Vuelva a intentarlo")
    

def MostrarMatrices ():
    while True:
        print("Mostrar matrices ")
        print("[1] Lista de matrices guardadas")
        print("[2] Mostrar contenido de una matriz ")
        print("[3] Salir")
        opcion = input("Seleccione opción: ")
        if opcion in ["1", "2", "3"]:
            return opcion
        else:
            print("Opción no válida!!! Vuelva a intentarlo")
    

def IngresoNumeroValido(mensajeUsuario, mensajeError):
    while(not (numero:=input(mensajeUsuario)).isdigit()):
        print(mensajeError)
    return int(numero)
