'''
Дан целочисленный список размера N. Найти максимальное количество его
одинаковых элементов.
'''
def max_count(number):
    elements = []
    element_counts = {}

    for i in range(number):
        elements.append(int(input(f"Введи число {i+int(1)} \n")))

    orig_arr = elements.copy()

    for element in elements:
        if element in element_counts:
            element_counts[element] += int(1)
        else:
            element_counts[element] = int(1)


    MAX_COUNT = max(element_counts.values())
    return MAX_COUNT, orig_arr


try:
    N = int(input("Введи размер списка \n"))
    if N < int(0):
        raise ValueError("Только целые, положительный числа. \n")
    resalt = max_count(N)
    print(f"Максимально одинаковых элементов - {resalt[int(0)]}")
    print(f"Изначальный список - {resalt[int(1)]}")
except ValueError as va:
    print(va)