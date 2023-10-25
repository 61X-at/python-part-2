guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

def main(guests_list):
    while True:
        length = len(guests_list)

        print(f'Сейчас на вечеринке {length} человек: {guests_list}')
        guest_move = input('Гость пришёл или ушёл? ')
        guest = input('Имя гостя: ')
        if guest_move == 'пришёл':
            guests_list = guest_come(guests_list, guest, length)
        elif guest_move == 'ушёл':
            guests_list = guest_left(guests_list, guest)
        else:
            print('Вечеринка закончилась, все легли спать.')
            break

def guest_come(guests, guest, list_len):
    if list_len == 6:
        print(f'Прости, {guest}, но мест нет.')
        return guests
    else:
        print(f'Привет, {guest}!')
        guests.append(guest)
        return guests
    
def guest_left(guests, guest):
    for i in guests:
        if i == guest:
            print(f'Пока, {guest}!')
            guests.remove(guest)
            return guests

main(guests)