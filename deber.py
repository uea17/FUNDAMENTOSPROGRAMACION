def search_value(matrix, value):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == value:
                return True, (i, j)
    return False, None

def main():
    # Definir la matriz
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Valor a buscar
    search_val = 5

    # Realizar la búsqueda
    found, position = search_value(matrix, search_val)

    # Mostrar el resultado
    if found:
        print(f"El valor {search_val} se encontró en la posición {position}")
    else:
        print(f"El valor {search_val} no se encontró en la matriz.")

if __name__ == "__main__":
    main()