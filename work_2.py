N = int(input("введите число : "))
nimb = []
for i in range(1, N+1) :
    square = i ** 2
    str_square = str(square)
    if str_square.endswith(str(i)):
        nimb.append(square)
print(f"good {N} : {nimb}")