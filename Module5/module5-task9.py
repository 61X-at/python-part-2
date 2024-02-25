def count_uppercase_lowercase(string):
    u_c = 0
    l_c = 0
    for i in string:
        if i.isupper() and i.isalpha():
            u_c += 1
        elif i.islower() and i.isalpha():
            l_c += 1
    return u_c, l_c


text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)