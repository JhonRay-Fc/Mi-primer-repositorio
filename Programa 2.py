# Definir la matriz bidimensional original de 3x3
matriz_original = [
    [10, 8, 20],
    [45, 12, 6],
    [7, 99, 81]
]

# Función para ordenar una fila de la matriz usando Bubble Sort
def ordenar_fila_bubble_sort(matriz, numero_fila):
    """
    Ordena una fila específica de la matriz en orden ascendente usando Bubble Sort.
    """
    # Validar que el número de fila sea válido
    if numero_fila < 0 or numero_fila >= len(matriz):
        print("Error: Número de fila no válido.")
        return

    fila_a_ordenar = matriz[numero_fila]
    n = len(fila_a_ordenar)

    # Implementación del algoritmo Bubble Sort
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila_a_ordenar[j] > fila_a_ordenar[j+1]:
                # Intercambiar los elementos
                fila_a_ordenar[j], fila_a_ordenar[j+1] = fila_a_ordenar[j+1], fila_a_ordenar[j]

    matriz[numero_fila] = fila_a_ordenar

# Mostrar la matriz original
print("Matriz Original:")
for fila in matriz_original:
    print(fila)

# Definir la fila a ordenar (ejemplo: la fila con índice 1)
fila_para_ordenar = 1

# Llamar a la función para ordenar la fila
ordenar_fila_bubble_sort(matriz_original, fila_para_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz_original:
    print(fila)