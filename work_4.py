N = int(input("Введите число:"))
i = 1
while True :
    square = i ** 2
    if square <= N :
        print(square , end = ' ')
        i +=1
    else:
        break
print()

for i in range(1 , N + 1):
    square = i ** 2
    if square <= N :
        print(square , end= ' ')
    else :
        break


