'''
Дан список размера N и целые числа К и L (1 < K < L < N ).
Найти среднее арифметическое элементов список с номерами от К до L включительно.
'''

def arithmetic_mean(numN, numK, numL):
    elements = []
    linit1 = numK
    linit2 = numL
    summ = int(0)
    count = int(0)

    for i in range(numN):
        elements.append(int(input(f"Введи число {i+int(1)} \n")))

    for j in elements:
        if elements[linit1] < j < elements[linit2]:
            summ += elements[j]
            count+= int(1)

    return int(summ / count)


try:
    N = int(input("Введи N размер списка:\n"))
    K = int(input("Введи K (1 < K < L < N):\n"))
    L = int(input("Введи L (1 < K < L < N):\n"))
    if  int(1) < K < L < N:
        raise ValueError("Условие 1 < K < L < N не выполняется")
    result = arithmetic_mean(N, K, L)
    print(result)
except ValueError as va:
    print(va)
