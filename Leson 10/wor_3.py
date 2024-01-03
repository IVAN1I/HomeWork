import random
my_dict = {}
dictt = {}

for i in range(1 ,11):
    key = 'key' + str(i)
    value = random.randint(1,100)
    cube = value ** 3

    my_dict[key] = cube
    dictt[key] = value
print("Изначальный словарь:", dictt)
print("Возведенный в куб:", my_dict)

