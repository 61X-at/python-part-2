while True:
    text = input('Придумайте пароль: ')
    length = len(text)
    if length < 8:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
        continue
    d_c = 0
    au_c = 0
    for i in range(length):
        if text[i].isdigit():
            d_c += 1
        elif text[i].isalpha() and text[i].isupper():
            au_c += 1
    if d_c > 2 and au_c > 0:
        print('Это надёжный пароль.')
        break
    print('Пароль ненадёжный. Попробуйте ещё раз.')
