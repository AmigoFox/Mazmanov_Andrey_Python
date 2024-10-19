# Даны два числа. Вывести вначале большее, а затем меньшее из
#них.
def exercise_one():
 num1=int(input("input number 1 \n"))
 num2=int(input("input number 2 \n"))
 num3=int(input("input number 3 \n"))
 if (num1==-num2 or num2==-num1 or num3==-num1 or
num3==-num2):
    print("Try repeat")
 else:
    print("No repepat")
exercise_one()
