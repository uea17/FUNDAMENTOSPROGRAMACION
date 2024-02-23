def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def sort_specific_row(matrix, row):
    bubble_sort(matrix[row])

def main():
    # Definir la matriz
    matrix = [
        [3, 1, 4],
        [1, 5, 9],
        [2, 6, 5]
    ]

    # Mostrar la matriz original
    print("Matriz original:")
    for row in matrix:
        print(row)

    # Ordenar una fila específica (por ejemplo, la primera fila)
    row_to_sort = 0
    sort_specific_row(matrix, row_to_sort)

    # Mostrar la matriz con la fila ordenada
    print("\nMatriz con la fila ordenada:")
    for row in matrix:
        print(row)

if __name__ == "__main__":
    main()
