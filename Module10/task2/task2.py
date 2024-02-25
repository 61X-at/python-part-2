import random
import os

total_sum = 0

if os.path.exists("out_file.txt"):
    os.remove("out_file.txt")

try:
    while total_sum < 777:
        user_number = int(input("Введите число: "))

        if random.randint(0, 13) == 6:
            raise TypeError

        total_sum += user_number
        
        with open("out_file.txt", "a", encoding="UTF-8") as file:
            file.write(str(user_number) + "\n")
except TypeError:
    print("Вас постигла неудача!")
else:
    print("Вы успешно выполнили условие для выхода из порочного цикла!")