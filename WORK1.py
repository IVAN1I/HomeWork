import random

N = int(input("Введите число N (больше 0): "))


if N <= 0:
    print("Число N должно быть больше 0.")
else:

    matrix = [[random.randint(10, 99) for _ in range(N)] for _ in range(N)]

    print("2-мерный список:")
    for row in matrix:
        print(row)

    sum_left_to_right = sum(matrix[i][i] for i in range(N))
    print("Сумма диагонали слева направо:", sum_left_to_right)

    sum_right_to_left = sum(matrix[i][N - 1 - i] for i in range(N))
    print("Сумма диагонали справа налево:", sum_right_to_left)

    center_value = matrix[N // 2][N // 2]
    print("Число в центре пересечения диагоналей:", center_value)
