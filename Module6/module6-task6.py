n = int(input('Введите кол-во заказов: '))

orders = {'Иванов': {}}

for i in range(n):
    order = input(f'{i+1} заказ: ').split()
    name = order[0]
    pizza = order[1]
    count = int(order[2])
    if name not in orders:
        orders[name] = {}
        orders[name][pizza] = count
    elif  pizza not in orders[name]:
        orders[name][pizza] = count
    else: 
        orders[name][pizza] += count

for i in orders:
    print(f'{i}:')
    for j in orders[i]:
        print(f'{j}: {orders[i][j]}')
