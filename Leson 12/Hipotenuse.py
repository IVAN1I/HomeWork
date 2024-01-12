hipotenuse = lambda x, y=1: (x**2 + y**2)**0.5

number1 = [3, 4, 5, 6]
resoult_1 = list(map(lambda x: hipotenuse(x), number1))
print("Пример 1 :", resoult_1)

number2_x = [1, 2, 3, 4]
number2_y = [2, 3, 4, 5]
resoult_2 = list(map(lambda x, y: hipotenuse(x, y), number2_x, number2_y))
print("Пример 2:", resoult_2)