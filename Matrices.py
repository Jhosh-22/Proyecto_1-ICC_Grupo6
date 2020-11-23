#Funcion de suma
def sumamatriz(matriz1,matriz2):
    matrizsuma = matrizvacia(len(matriz1),len(matriz2[0]))
    for fila in range(len(matriz1)):
        for col in range(len(matriz1[1])):
            matrizsuma[fila][col] = matriz1[fila][col] + matriz2[fila][col]
    print("La matriz resultante es: ")
    return matrizsuma
#Funcion de resta
def restamatriz(matriz1,matriz2):
    matrizrest =matrizvacia(len(matriz1),len(matriz2[0]))
    for fila in range(len(matriz1)):
        for col in range(len(matriz2[1])):
            matrizrest[fila][col] = matriz1[fila][col] - matriz2[fila][col]
    print("La matriz resultante es: ")
    return matrizrest
#Funcion de multiplicacion
def multiplicacion(matriz1, matriz2):
    matrizmulti = matrizvacia(len(matriz1), len(matriz2[0]))
    if len(matriz1[0]) == len(matriz2):
        for i in range(len(matriz1)):
            for j in range(len(matriz2[0])):
                for k in range(len(matriz2)):
                    matrizmulti[i][j] += matriz1[i][k] * matriz2[k][j]
        print("La matriz resultante es: ")
        return matrizmulti
    else:
        return ("Recuerda que la multiplicacion entre matrices debe ser mxn * nxp")

#Funcion de trasposicion de matriz determinada
def trasponerMatrices(matriz):
    matriztras = []
    for fila in range(len(matriz[0])):
        matriztras.append([])
        for col in range(len(matriz)):
            matriztras[fila].append(matriz[col][fila])
    print("La matriz traspuesta es: ")
    return matriztras
#Creador de la matriz para la resolucion de las operaciones
def matrizvacia(m,n):
    matrizvacia = []
    for i in range(m):
        row=[]
        for j in range(n):
            row.append(0)
        matrizvacia.append(row)
    return matrizvacia