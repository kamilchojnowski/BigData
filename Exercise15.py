print("Insert filepath: ")
path = input()
try:
    file = open(path, "r")
except FileNotFoundError:
    print("File not found")
    
data = file.read()
print(f"C+G is {((data.count('C')+data.count('G'))/len(data))*100}%")