input_number = int(input("Введите число от 1 до 9:"))
if input_number < 1 or input_number > 9 :
    print  ("введите другое число ")
else :
    for i in range (1 , input_number + 1) :
        increasing_numbers = "".join (str(j) for j in range(1 ,i +1))
        decreasing_numbers = "".join (str(j) for j in range (i -1 , 0 , -1 ))

        line = f"{increasing_numbers} {decreasing_numbers}"
        print(line.ljust(input_number ))

