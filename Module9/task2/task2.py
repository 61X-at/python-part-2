file = open('zen.txt', 'r', encoding='UTF-8')

res = file.readlines()

for i in range(len(res)):
    print(res[-i - 1])