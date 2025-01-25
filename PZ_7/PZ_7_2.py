'''Дана строка, состоящая из русских слов, набранных заглавными буквами и разделенных пробелами
(одним или несколькими). Преобразовать каждое слово в строке, заменив в нем все последующие вхождения его первой буквы
на символ «.» (точка). Например, слово «МИНИМУМ» надо преобразовать в «МИНИ.У». Количество пробелов между словами не изменять.'''

def transform_string(input_string):
    result = []
    for word in input_string.split(' '):
        if word:
            first_char = word[0]
            transformed_word = first_char + word[1:].replace(first_char, '.')
            result.append(transformed_word)
        else:
            result.append('')
    return ' '.join(result)

try:
    input_string = input("Введите строку из русских слов, разделенных пробелами: ")
    if not input_string.strip():
        raise ValueError("Строка не должна быть пустой.")

    result = transform_string(input_string)
    print(f"Результат: {result}")
except ValueError as ve:
    print(ve)