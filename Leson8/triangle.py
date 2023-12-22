num_lines = int(input("Введиете длину строки :"))
for i in range (1 , num_lines + 1) :

    spaces = " " * (num_lines - i)
    numbers = "0" * i
    line = f"{i}{spaces} {numbers}"

    print(line)