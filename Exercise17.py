import random

def triangle_and_print(x: int):
    print(x, x*x*x)
    
for _ in range(50):
    triangle_and_print(random.randint(1, 1000))