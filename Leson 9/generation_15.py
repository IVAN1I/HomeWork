import random

number = [random.randint (1 , 100) for _ in range(15)]

even_number = [ num for num in number if num % 2 == 0]
odd_number = [ num for num in number if num % 2 != 0]

if sum(odd_number) > sum (even_number) :
    print ("Yes")
else :
    print("No")

print("number" , number)
print("even number" , even_number)
print("odd number" , odd_number)