import random
import string

path = "mutant.txt"

def get_string():
    return "".join(random.choice(string.ascii_uppercase) for _ in range(50))

def get_sum(s: str):
    sum = 0
    for c in s:
        sum += ord(c)
    return sum

def generate():
    file = open(path, "a+")
    for _ in range(300):
        file.write(get_string())
        file.write("\n")
    file.close()
    
def count():
    file = open(path, "r")
    fl = file.readlines()
    for l in fl:
        print(f"{l}count: {get_sum(l)}")
        
generate()
count()

