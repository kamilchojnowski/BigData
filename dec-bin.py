def to_binary(x):
    return bin(x) 

print("Insert a number:")
try:
    a = int(input())
except ValueError:
    print(f"{a} is not a number")
    exit()
print(f"{a} binary is {to_binary(a)}")
