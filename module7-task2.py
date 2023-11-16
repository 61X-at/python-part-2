def is_prime(num):
    if num == 0 or num == 1:
        return False
    return all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

def crypto(obj):
    return [item for i, item in enumerate(obj) if is_prime(i)]

print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))