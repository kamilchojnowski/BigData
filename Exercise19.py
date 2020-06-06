import random
import time
import numpy

print("Insert matrixes sizes")
print("M:")
M = int(input())
print("N:")
N = int(input())

start = time.time()

matrix_m = numpy.random.randint(1, 14, (M,N))
matrix_n = numpy.random.randint(1, 14, (M,N))

print(matrix_m)
print(matrix_n)
print(matrix_m + matrix_n)

print(time.time() - start)
