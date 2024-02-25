s_h = 0
e_h = 0

text = input('Введите строку: ')

for i in range(len(text)):
    if text[i] == 'h':
        s_h = i + 1
        for i in range(1, len(text) + 1):
            if text[-i] == 'h':
                e_h = len(text) - i
                break
    break
    
print(text[s_h:e_h][::-1])