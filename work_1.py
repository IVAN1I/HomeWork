lst =list(input("Введите цифры:"))

for i in lst :
    if  lst.count(i) >1:
        print("Есть совпадения")
        break
else :
    print("Нет совпадений")