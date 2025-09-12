# Definir la matriz bidimensional 3x3
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Valor que queremos buscar
valor_buscado = 50

# Función para realizar la búsqueda
def buscar_valor(matriz, valor):
    """
    Realiza una búsqueda lineal en una matriz para encontrar un valor.
    Devuelve la posición (fila, columna) si se encuentra, o (-1, -1) si no.
    """
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == valor:
                return fila, columna
    return -1, -1

# Llamar a la función y mostrar el resultado
posicion = buscar_valor(matriz, valor_buscado)

if posicion != (-1, -1):
    print(f"El valor {valor_buscado} se encontró en la posición: Fila {posicion[0]}, Columna {posicion[1]}")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")