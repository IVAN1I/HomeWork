import random

def generate_2d_list(rows=None, clos=None):
    if rows is None:
        rows = random.randint(2,5)
    if clos is None:
        clos = random.randint(3,7)

    two_d_list = [[random.randint(0,200)for _ in range(clos)]for _ in range(rows)]
    return two_d_list

def print_symmetric_table(two_d_list):
    for row in two_d_list:
        print(" ".join(map(str, row)))

table1 = generate_2d_list()
print("Табличка 1:")
print_symmetric_table(table1)
print("\n" + "-" * 20 + "\n")

table2 = generate_2d_list(rows=4)
print("Табличка 2:")
print_symmetric_table(table2)
print("\n" + "-" * 20 + "\n")

table3 = generate_2d_list(rows=3, clos=6)
print("Табличка 3:")
print_symmetric_table(table3)
print("\n" + "-" * 20 + "\n")

