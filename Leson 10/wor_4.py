import random

my_dict = {}

list_one = [random.randint(1, 100)for _ in range(10)]
list_two = [random.randint(1, 100)for _ in range(10)]

my_dict = dict(zip(list_one , list_two))
print(my_dict)