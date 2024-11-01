try:
  number = int(input("Введи число "))
  hundreds = number // 100
  tens = (number % 100) // 10
  units = number % 10
  new_number = tens * 100 + hundreds * 10 + units
  print("Измененное число:", new_number)
except ValueError:
  print("Нельзя вводить текст! Введите целое число.")
