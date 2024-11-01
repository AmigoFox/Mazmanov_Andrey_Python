# Проверить истинность высказывания: «Среди трех данных целых чисел есть хотя бы
#одна пара взаимно противоположных».
def exercise_one():
    try:
     num1=int(input("введи число 1 \n"))
     num2=int(input("введи число 2 \n"))
     num3=int(input("введи число 3 \n"))
     if (num1==-num2 or num2==-num1 or num3==-num1 or
    num3==-num2):
        print("Есть повтор")
     else:
        print("Нет повтора")
    except ValueError:
        print("только числа")

exercise_one()