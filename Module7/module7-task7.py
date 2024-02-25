print('Строка: abcd')
print('Кортеж чисел: (10, 20, 30, 40)')

string = 'abcd'
nums = (10,20,30,40)

res = ((string[i], nums[i]) for i in range(min(len(string),len(nums))))

print(res)

for i in res:
    print(i)