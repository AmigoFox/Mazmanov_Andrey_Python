# Даны 2 числа. Вывести вначале большее, затем меньшее
try:
 num1 = int(input("введи число 1 \n"))
 num2 = int(input("введи число 2 \n"))

 if num1 > num2:
  print("число 1 больше :", num1)
  print("число 2 меньше :", num2)
 else:
  print("число 2 больше :", num2)
  print("число 1 меньше :", num1)

except ValueError:
 print("Только числа")
