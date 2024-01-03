import random
my_dict = {}
product_resoult = 1

for i in range(1 ,21):
    key = 'key' + str(i)
    value = random.randint(1,10)

    product_resoult *= value
    my_dict[key] = value

print("Словарь :", my_dict)
print("Сумма умножения :", product_resoult)

