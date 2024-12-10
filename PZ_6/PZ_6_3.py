'''
Дан список размера N, все элементы которого, кроме одного, упорядочены по убыванию.
Сделать список упорядоченным, переместив элемент, нарушающий упорядоченность, на новую позицию.
'''
def bubble_sort(number):
    elements = []
    for i in range(number):
        elements.append(int(input(f"Введи число {i+int(1)} \n")))

    arr = len(elements)
    arr_orig = elements.copy()

    for j in range(arr):
        for elem in range(int(0), arr-j-int(1)):
            if elements[elem] > elements[elem + int(1)]:
                elements[elem + int(1)] ,elements[elem] = elements[elem], elements[elem+1]
    return elements, arr_orig

try:
    N = int(input("Введи размер списка \n"))
    if N < int(0):
        raise ValueError("Только целые, положительный числа. \n")
    resalt = bubble_sort(N)
    print(f"Изначальный список - {resalt[int(1)]}")
    print(f"Отсортированный список - {resalt[int(0)]}")
except ValueError as va:
    print(va)