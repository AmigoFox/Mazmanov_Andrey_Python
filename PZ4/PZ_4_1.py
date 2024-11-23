#Дано вещественное число X и целое число N (> 0). Найти значение выражения
# 1 - X2/(2!) + X4/(4!) - … + (-1) -X2*/((2-N)!) (N! = 12 ... N).
# Полученное число является приближенным значением функции cos в точке X.
import math
try:
    x = float(input("Введите вещественное число X: "))
    n = int(input("Введите целое число N (> 0): "))
    if n <= 0 and float(x):
        raise ValueError
except ValueError:
    print("Только числа n > 0 и число х дробное число")
else:
    count = 0
    for k in range(n + 1):
        term = ((-1) ** k) * (x ** (2 * k)) / math.factorial(2 * k)
        count += term
    print(count)