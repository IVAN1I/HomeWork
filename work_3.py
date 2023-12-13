sum_numbers = 0
count_numbers = 0
max_value = float('-inf')
min_value = float('inf')
even_count = 0
odd_count = 0

while True :
    num =  int(input("Введите любое число , или 0 для завершения программы :"))
    if num == 0 :
        break
    sum_numbers += num
    count_numbers += 1

    if num > max_value :
        max_value = num
    if num < min_value :
        min_value = num
    if num % 2 == 0 :
        even_count += 1
    else :
        odd_count += 1
    average = sum_numbers / count_numbers if count_numbers != 0 else 0
print ("сумма чисел:" ,sum_numbers)
print("среднне арифм.:",average)
print("максимальное значение:" ,max_value)
print("минимальное значение:",min_value)
print("парные:",even_count)
print("не парные :", odd_count)


