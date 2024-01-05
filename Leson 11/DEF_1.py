def find_sum_pair(numbers, target_sum):
    sen_numbers = set()
    for num in numbers:
        complement = target_sum - num
        if complement in sen_numbers:
            return True
        sen_numbers.add(num)
    return False

numbers_1 = [1,2,3,4,5]
target_sum_1 = 9
resoult_1 = find_sum_pair(numbers_1 , target_sum_1)
print(f' Пример 1 - {resoult_1}')

numbers_2 = [5,3,5,1,7]
target_sum_2 = 9
resoult_2 = find_sum_pair(numbers_2 , target_sum_2)
print(f' Пример 2 - {resoult_2}')