from pprint import pprint
matrix = [[0] * 5 for _ in range (5)]
for i in range(5):
    matrix [i][i] = 10 + i
for i in range(5):
    matrix [i][4-i] = 14 - i
pprint(matrix)
