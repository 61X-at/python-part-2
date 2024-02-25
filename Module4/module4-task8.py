alphabet = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']


text = input('Введите сообщение: ')
n = int(input('Введите сдвиг: '))

new_message = [alphabet[(alphabet.index(j) + n) % len(alphabet)] for i in text.split(' ') for j in i]

for i in range(len(text)):
    if text[i] == ' ':
        new_message.insert(i, ' ')

print(''.join(new_message))