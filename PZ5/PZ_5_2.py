'''Дан прямоугольник, длины сторон которого равны натуральным числам А и В.
Составить функцию, которая будет находить на сколько квадратов
можно разрезать данный прямоугольник,
 если от него каждый раз отрезать квадрат наибольшей площади.'''
def count_squares(a, b):
    if not (isinstance(a, int) and isinstance(b, int) and a > 0 and b > 0):
        return -1

    count = 0
    while a > 0 and b > 0:
        side = min(a, b)
        count += 1
        a = a - side if a >= b else a
        b = b - side if b >= a else b
    return count

while True:
    try:
        a = int(input("Введите длину стороны A: "))
        b = int(input("Введите длину стороны B: "))
        if a <= 0 or b <= 0:
            raise ValueError("Длины сторон должны быть положительными числами.")
        result = count_squares(a, b)
        if result == -1:
            print("Ошибка: Введите положительные целые числа.")
        else:
            print(f"Можно вырезать {result} квадратов.")
            break
    except ValueError:
        print("Ошибка: ")