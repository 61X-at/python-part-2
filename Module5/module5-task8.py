def get_shifted_string(string, offset):
    return "".join(["".join(string[offset:]), "".join(string[:offset])])


first = input("Первая строка: ")
second = input("Вторая строка: ")

for i in range(len(first)):
    if get_shifted_string(first, i) == second:
        print(f"Первая строка получается из второй со сдвигом {i}")
        break
else:
    print("Первую строку нельзя получить из второй с помощью циклического сдвига")