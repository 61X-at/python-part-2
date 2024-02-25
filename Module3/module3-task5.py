violator_songs = [['World in My Eyes', 4.86],['Sweetest Perfection', 4.43],['Personal Jesus', 4.56],['Halo', 4.9],
    ['Waiting for the Night', 6.07],['Enjoy the Silence', 4.20],['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],['Clean', 5.83]]

count_songs = int(input('Сколько песен выбрать? '))
time_sum = 0

for i in range(count_songs):
    name_song = input(f'Название {i+1}-й песни: ')
    for i in violator_songs:
        if i[0] == name_song:
            time_sum += i[1]
            break

print(f'Общее время звучания песен — {round(time_sum, 2)} минуты')
