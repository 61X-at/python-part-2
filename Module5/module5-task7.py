str = input('Введите IP: ').split('.')
error = False
for i in str:
    if not i.isdigit():
        print(f'{i} — это не целое число.')
        error = True
        break
    elif len(str) != 4:
        print('Адрес — это четыре числа, разделённые точками.')
        error = True
        break
    elif int(i) > 255:
        print(f'{i} превышает 255.')
        error = True
        break

if not error:
    print('IP-адрес корректен.')