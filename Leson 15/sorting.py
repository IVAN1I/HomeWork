import random

def generate_matrix(size):
    return [[random.randint(1, 50) for _ in range(size)] for _ in range(size)]

def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(f"{elem:2}", end=" ")
        print()

def sort_matrix(matrix):
    column_sums = [sum(column) for column in zip(*matrix)]

    for i in range(len(column_sums)):
        for j in range(len(column_sums) - 1):
            if column_sums[j] > column_sums[j + 1]:
                # Сортировка столбцов по суммам
                column_sums[j], column_sums[j + 1] = column_sums[j + 1], column_sums[j]
                for k in range(len(matrix)):
                    matrix[k][j], matrix[k][j + 1] = matrix[k][j + 1], matrix[k][j]

    for j in range(len(matrix[0])):
        # Сортировка каждого нечетного столбца по возрастанию значений снизу вверх
        if j % 2 != 0:
            column_values = [matrix[i][j] for i in range(len(matrix))]
            column_values.sort(reverse=True)
            for i in range(len(matrix)):
                matrix[i][j] = column_values[i]
        else:
            # Сортировка каждого четного столбца по возрастанию значений сверху вниз
            column_values = [matrix[i][j] for i in range(len(matrix))]
            column_values.sort()
            for i in range(len(matrix)):
                matrix[i][j] = column_values[i]

def main():
    size = int(input("Введите размер матрицы (M > 5): "))
    if size <= 5:
        print("Пожалуйста, введите число больше 5.")
        return

    matrix = generate_matrix(size)

    print("Исходная матрица:")
    print_matrix(matrix)

    sort_matrix(matrix)

    print("\nОтсортированная матрица:")
    print_matrix(matrix)

if __name__ == "__main__":
    main()
