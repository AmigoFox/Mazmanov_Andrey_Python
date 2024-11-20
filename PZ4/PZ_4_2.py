# найти факториал N (> 0). Найти сумму 1 ** 1 + 2**2 + ... + N ** N
try:
    number = int(input("Введи положительное целое цисло \n"))
    if number <= 0:
        raise ValueError
except ValueError:
    print("Только положительные числа")# если уже ввели буквы
else:
    count = 0
    for i in range(1, number + 1):
        count = count + (i ** i)
    print(count, "count")