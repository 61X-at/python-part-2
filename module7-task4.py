import random 

original = [random.randint(1, 100) for _ in range(10)]

print([(original[i],original[i+1]) for i in range(0,10,2)])