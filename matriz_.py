# Matriz bidimensional de 3x3
matriz = [
    [5, 8, 2],
    [6, 7, 4],
    [9, 1, 3]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j  # Retorna la posición (fila, columna)
    return None  # Si no se encuentra el valor

# Valor específico a buscar
valor_buscado = 7

# Búsqueda del valor
posicion = buscar_valor(matriz, valor_buscado)

# Resultado
if posicion:
    print(f"El valor {valor_buscado} se encontró en la posición fila {posicion[0]}, columna {posicion[1]}.")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")
