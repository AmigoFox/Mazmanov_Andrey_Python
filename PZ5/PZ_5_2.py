'''Дан прямоугольник, длины сторон которого равны натуральным числам А и В.
Составить функцию, которая будет находить на сколько квадратов
можно разрезать данный прямоугольник,
 если от него каждый раз отрезать квадрат наибольшей площади.'''
def count_squares(a, b):
    count = 0
    while a > 0 and b > 0:
        side = min(a, b)
        count += 1
        a = a - side if a >= b else a
        b = b - side if b >= a else b
    return count

try:
    a = int(input("Введите длину стороны A: "))
    b = int(input("Введите длину стороны B: "))
    if a <= 0 and b <= 0:
        raise ValueError("Ошибка: Только целые, положительные числа!")
    result = count_squares(a, b)
    print(f"Можно вырезать {result} квадратов.")
except ValueError as ve:
    print(ve)