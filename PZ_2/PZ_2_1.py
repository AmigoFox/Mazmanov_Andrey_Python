# Дано 3х значное число. Вывести число при перестановке цифр сотен и десятков исходного числа (например 123 -> 213) 
try:
  number = int(input("Введи число "))
  hundreds = number // 100
  tens = (number % 100) // 10
  units = number % 10
  new_number = tens * 100 + hundreds * 10 + units
  print("Измененное число:", new_number)
except ValueError:
  print("Нельзя вводить текст! Введите целое число.")


print("Нельзя вводить текст! Введите целое число.")
