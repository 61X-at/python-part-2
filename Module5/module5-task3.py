file = input('Название файла: ')

wrong_start = ['@', '№', '$', '%', '^', '&', '*', '(', ')']
wrong_end = ['.txt', '.docx']

if file[0] in wrong_start:
    print('Ошибка: название начинается недопустимым символом.')
elif not (file.endswith(".txt") or file.endswith(".docx")):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно.')