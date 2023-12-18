my_string = list(input("введите 15 символов :"))
if not my_string :
    print("Строка пустая.")

if len(my_string) < 15 :
    my_string = my_string * 3
print(my_string)

last5 = my_string[-5:]
print(last5)

revers_list = my_string[::-1]
print(revers_list)

five_end_five = last5 + last5
print(five_end_five)

last_elements = my_string[:-2] , my_string[2:]
print(last_elements)


