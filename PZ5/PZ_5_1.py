#создать def которая напечатает любые 40 символов
import random
# 33-255 ищи в диапазане (для себя)
def randon_letter():
    letters = []
    for i in range(1, 41):
        letters.append((i, chr(random.randint(8000, 8255))))
    return letters

all_letters = randon_letter()
for i, letter in all_letters:
    print(f"{i}: {letter}")