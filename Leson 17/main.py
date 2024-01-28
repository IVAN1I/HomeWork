from Leson9 import generation_15
from Leson8 import Calculate




def process_values():
    """
    Запрашивает ввод двух значений и выполняет конкатенацию или сумму в зависимости от их типа.
    Возвращает результат операции.
    """
    try:

        value1 = input("Введите первое значение: ")
        value2 = input("Введите второе значение: ")


        num1 = float(value1)
        num2 = float(value2)


        result = num1 + num2
        return f"Сумма чисел: {result}"

    except ValueError:

        result = str(value1) + str(value2)
        return f"Конкатенация значений: {result}"


print(process_values())

print(generation_15)
print(Calculate)
