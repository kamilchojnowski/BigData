print("Enter filepath:")
path = input()
try:
    file = open(path, "r")
except FileNotFoundError:
    print("File not found")
    exit()

data = file.read()
file.close()
new_data = "".join([chr(ord(d)+1) for d in data])
file = open(path, "w")
file.write(new_data)
file.close()

