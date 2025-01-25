'''Вариант 20.
Используя словарь посчитать количество уникальных слов в заданном предложении «Изучаем язык Питон». Вывести на экран каждую пару
«ключ:значение».'''

def dictionary(STR):
    dictionary = {}
    for word in STR.split(' '):
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary

try:
    input_string = input("Введите предложение: ")
    if not input_string.strip():
        raise ValueError("Введи предложение, а не оставь его пустым")
    result = dictionary(input_string)
    for key, value in result.items():
        print(f"{key}: {value}")
except ValueError as va:
    print(va)