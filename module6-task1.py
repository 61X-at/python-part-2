violator_songs = {
'World in My Eyes': 4.86,
'Sweetest Perfection': 4.43,
'Personal Jesus': 4.56,
'Halo': 4.9,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.20,
'Policy of Truth': 4.76,
'Blue Dress': 4.29,
'Clean': 5.83
}

n = int(input('Введите кол-во песен: '))

sum_time = 0

for i in range(n):
    sum_time += violator_songs[input('Введите название песни: ')]

print(round(sum_time, 2))