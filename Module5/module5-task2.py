text = input('Введите строку: ').split()

max_len_str = 0
max_str = ''

for i in text:
    if len(i) > max_len_str:
        max_len_str = len(i)
        max_str = i

print(f'Самое длинное слово: "{max_str}.')
print(f'Длина этого слова: {max_len_str} символ.')