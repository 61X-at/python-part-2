print('Введите значения оригинального словаря частот(чтобы прекратить ввод отправьте пустую строку два раза)')
print('Оригинальный словарь частот: ')

dictionary  = {}

while True:
    s = input()
    if s == '':
        c += 1
        if c > 1:
            break
    else:
        s = s.replace(' ', '').split(':')
        if s[1] in dictionary:
            dictionary[s[1]].append(s[0])
        else:
            dictionary[s[1]] = []
            dictionary[s[1]].append(s[0])
    
        c = 0

for i in dictionary:
    print(f'{i} - {dictionary[i]}') 