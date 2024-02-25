vowels_list = ['а', 'у', 'е', 'ы', 'о', 'э', 'я', 'и', 'ю']

vowels_in_text = []

text = input('Введите текст: ')

for i in text:
    if i in vowels_list:
        vowels_in_text.append(i)

print(f'Список гласных букв: {vowels_in_text}')
print(f'Длина списка: {len(vowels_in_text)}')