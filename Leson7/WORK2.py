import random
import pprint
N = int(input("Вваедите число N (больше 5):"))
M = int(input("Введите число M (больше 5):"))
if N <=5 or M <=5 :
    print("Введите другое число")
    exit()
matrix =[[random.randint(1 ,100) for _ in range (N)]for _ in range (M)]
pprint.pprint (matrix)

for row in matrix :
    row[-1],row[-2] = row[-2],row[-1]
print("после замены столбцов")
for row in matrix :
    print(row)

