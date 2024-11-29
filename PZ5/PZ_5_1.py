#создать def которая напечатает любые 40 символов
import random
# 33, 255 ищи в диапазане
def randon_letter():
    for i in range(1,40+1):
        print(i, chr(random.randint(33,255)))

randon_letter()