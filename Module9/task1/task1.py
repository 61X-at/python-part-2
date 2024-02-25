file = open('numbers.txt', 'r', encoding='UTF-8')

summ = 0

for i in file:
    summ += int(i)

res = open('answer.txt', 'w', encoding='UTF-8')

res.write(str(summ))

file.close()
res.close()
