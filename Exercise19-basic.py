import random
import time

print("Insert matrixes sizes")
print("M:")
M = int(input())
print("N:")
N = int(input())

start = time.time()

matrix_m, matrix_n, matrix_sum = [], [], []

for m in range(M):
    temp_m, temp_n, temp_sum = [], [], []
    for n in range(N):
        temp_n.append(random.randint(1, 14))
        temp_m.append(random.randint(1, 14))
        temp_sum.append(temp_n[n] + temp_m[n])
    matrix_n.append(temp_n) 
    matrix_m.append(temp_m)
    matrix_sum.append(temp_sum)
            
print(matrix_m)
print(matrix_n)
print(matrix_sum)
print(f"Time: {time.time()-start}")

