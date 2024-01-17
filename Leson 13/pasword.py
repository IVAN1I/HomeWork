def decorator(function):
    def wrapper():
        while True:
            print("Требования к паролю: минимум 1 цифра, 1 буква, 1 специальный символ, длина не менее 8 символов.")
            password = function()
            if password is None :
                continue
            if any(c.isdigit()for c in password)and any(c.isalpha()for c in password)\
                and any(c in "!@#$%^&*()-_=+[]{};:'\",.<>?/" for c in password) \
                and len(password) >=8:
                print("Пароль соответствует требованиям.")
                return password
        else:
            print("Пароль не соответствует требованиям. Попробуйте еще раз.")
    return wrapper()

@decorator
def get_password ():
    password =input("Введите пароль : ")

    if not password or any(c.isspace()for c in  password):
        print("Пароль не может быть пустым или содержать пробельные символы.")
        return None
    return password




