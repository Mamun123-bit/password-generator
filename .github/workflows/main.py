import random
import string

def generate_password():
    # Символы для пароля: латиница, цифры и специальные символы
    characters = string.ascii_letters + string.digits + '@_#$)!'
    
    # Обязательно включаем одну заглавную, одну строчную букву, одну цифру и один спецсимвол
    password = [
        random.choice(string.ascii_uppercase),  # одна заглавная буква
        random.choice(string.ascii_lowercase),  # одна строчная буква
        random.choice(string.digits),           # одна цифра
        random.choice('@_#$)!')                 # один специальный символ
    ]
    
    # Дополняем пароль случайными символами до длины от 13 до 15
    password_length = random.randint(13, 15)
    password += [random.choice(characters) for _ in range(password_length - 4)]
    
    # Перемешиваем символы в пароле
    random.shuffle(password)
    
    return ''.join(password)

def generate_passwords_to_file(number_of_passwords, filename):
    with open(filename, 'w') as file:
        for _ in range(number_of_passwords):
            password = generate_password()
            file.write(password + '\n')
    print(f"{number_of_passwords} паролей сгенерировано и записано в файл '{filename}'.")
    print("Спасибо за использование скрипта!")
    print_stylized_bot_message()

def print_stylized_bot_message():
    # Стилизованный вывод с использованием спецсимволов
    print("\n" + "*" * 40)
    print("*" + " " * 10 + "@BuyKYC_bot" + " " * 10 + "*")
    print("*" * 40)
    print("KYC, Proxy, Аккаунты соц сетей: @BuyKYC_bot")
    print("*" * 40)

# Основная часть программы
try:
    number_of_passwords = int(input("Введите количество паролей, которые нужно сгенерировать: "))
    filename = input("Введите название файла для сохранения паролей (например, 'passwords.txt'): ")
    
    # Генерируем и записываем пароли в файл
    generate_passwords_to_file(number_of_passwords, filename)

except ValueError:
    print("Пожалуйста, введите корректное число.")
