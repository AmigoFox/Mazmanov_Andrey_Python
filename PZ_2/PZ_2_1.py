# Вариант20. Дано 3-х значное число. Вывести число полученное при 
#перестановке цифр исходного числа
number = int(input("inpyt num "))
hundreds = number // 100
tens = (number % 100) // 10
units = number % 10
new_number = tens * 100 + hundreds * 10 + units
print("Number with rearranged hundreds digits and base:", new_number)
