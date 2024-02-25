rollers = []
people_foot_size = []

r_count = int(input('Количество роликов: '))
for i in range(r_count):
    rollers.append(int(input(f'Размер пары {i+1}: ')))

p_count = int(input('Количество людей: '))
for i in range(p_count):
    people_foot_size.append(int(input(f'Размер пары {i+1}: ')))

count = 0

for i in people_foot_size:
    for j in rollers:
        if i == j:
            count += 1
            rollers.remove(j)

print(f'Наибольшее количество людей, которые могут взять ролики: {count}')