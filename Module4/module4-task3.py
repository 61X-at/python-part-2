import random


list1 = []
list2 = []
result = []

for i in range(20):
    list1.append(round(random.uniform(5,10), 2))
    list2.append(round(random.uniform(5,10), 2))

for i in range(20):
    result.append(max(list1[i],list2[i]))

print(f'Первая команда: {list1}')
print(f'Вторая команда: {list2}')
print(f'Победители тура: {result}')