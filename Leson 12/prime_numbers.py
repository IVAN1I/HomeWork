def is_prime(num):
    if num < 2 :
        return False
    for i in range (2,int(num ** 0.5) +1):
        if num % i == 0 :
            return True
    return False

def prime_generator(n, z):
    for number in range(max(2, n), z+1):
        if is_prime(number):
            yield number

import random

n=random.randint(1,50)
z=random.randint(n,100)
print(f"Диапазон: от {n} до {z}")
result = list(prime_generator(n, z))
print("Простые числа:", result)
