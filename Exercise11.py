import random

start, stop = 1, 100
max_length = 100
count = 0
bpoint = 23

data = [random.randint(start, stop) for _ in range(max_length)]
for i in data:
    count = count + 1 if i < bpoint else count
    
data.sort()
print(data)
print(count)