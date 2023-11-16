def printer(n):
    if n > 1:
        printer(n - 1)
    print(n)

n = int(input('Введите число: '))

printer(n)