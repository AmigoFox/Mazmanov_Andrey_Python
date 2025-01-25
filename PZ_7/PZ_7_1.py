'''Дано целое положительное число. Вывести символы изображающие это число '''

def Num(num):
    str_num = ''
    for digit in str(num):
        str_num += digit
        str_num += " "
    return str_num.strip()

try:
    number = int(input("Введите целое положительное число: "))
    if number <= 0:
        raise ValueError("Число должно быть положительным.")
    result = Num(number)
    print(f"Результат: {result}")
except ValueError as va:
    print(va)