def show_contacts(dict):
    print('Текущий словарь контактов:')
    print('ИМЯ ФАМИЛИЯ ТЕЛЕФОН')
    for name, surname in dict:
        res = name + ' ' + surname + ' ' + str(dict[(name, surname)])
        print(res)

def searcher(dict, search):
    c = 0
    print('Произвожу поиск...')
    for name, surname in dict:
        if search == surname:
            res = name + ' ' + surname + ' ' + str(dict[(name, surname)])
            print(res)
            c += 1
    print(f'Было найдено {c} контактов с фамилией {search}')

def main():
    dict = {}

    while True:
        cm = int(input('Введите номер действия: \n1. Добавить контакт.\n2. Найти человека.\n'))
        if cm == 1:
            name = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').split())
            if len(name) < 2:
                print('Непраивльный ввод')
                continue
            if name in dict:
                print('Такой человек уже есть в контактах.')
                show_contacts(dict)
                continue
            phone = int(input('Введите номер телефона: '))
            dict[name] = phone
            show_contacts(dict)
        elif cm == 2:
            surname = input('Введите фамилию для поиска: ')
            searcher(dict, surname)
        else:
            print('Введена неправильная команда')

main()