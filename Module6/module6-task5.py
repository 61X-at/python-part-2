n = int(input('Введите кол-во пар: '))

synonyms = {}

for i in range(n):
    s = input().lower().replace(' ', '').split("—")
    synonyms[s[0]] = s[1]
    synonyms[s[1]] = s[0]

word = input('Введите слово: ').lower()

if word in synonyms:
    print(f'Синоним: {synonyms[word]}')
else:
    print('Такого слова в словаре нет.')