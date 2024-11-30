'''Дан прямоугольник, длины сторон которого равны натуральным числам А и В.
Составить функцию, которая будет находить на сколько квадратов
можно разрезать данный прямоугольник,
 если от него каждый раз отрезать квадрат наибольшей площади.'''
import numbers

def rec(A, B):
    print(f"Сторона A: {A}")
    print(f"Сторона B: {B}")

def get_rectangle_sides():
    try:
        A = int(input('Введите сторону прямоугольника A (натуральное число): '))
        B = int(input('Введите сторону прямоугольника B (натуральное число): '))
        if not (isinstance(A, numbers.Integral) and A > 0 and isinstance(B, numbers.Integral) and B > 0):
            raise ValueError("Введите натуральные числа, больше 0")
        return A, B
    except ValueError as e:
        print(f"Ошибка: {e}")
        return get_rectangle_sides()  # Recursive call for invalid input

A, B = get_rectangle_sides()
rec(A, B)
