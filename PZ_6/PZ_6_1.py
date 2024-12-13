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

    for j in range(linit1, linit2 + 1):
        summ += elements[j]
        count += int(1)

    return float(summ / count)


try:
    N = int(input("Введи N размер списка:\n"))
    K = int(input("Введи K (1 < K < L < N):\n"))
    L = int(input("Введи L (1 < K < L < N):\n"))
    if  not (int(1) < K < L < N):
        raise ValueError("Условие 1 < K < L < N не выполняется")
    result = arithmetic_mean(N, K, L)
    print(f"Результат --, {result}")
except ValueError as va:
    print(va)