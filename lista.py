try:
    file = open("lista.txt", "r")
except FileNotFoundError:
    print("No file 'lista.txt' found")
else:
    print("Name, Surname, Group")
    for line in file.readlines():
        print(line)
    file.close()
    
file = open("lista.txt", "a+")
is_adding_next = True
print("Insert new students:")
students = []
while(is_adding_next):
    print("Name:")
    name = input()
    print("Surname:")
    surname = input()
    print("Group:")
    group = input()
    students.append((name, surname, group))
    print("Do you want to add next srudent? [y/n]")
    answer = input()
    while(answer not in ["y", "n"]):
        print("Please enter 'y' or 'n'")
        answer = input()
    if answer == "n":
        is_adding_next = False
        
for s in students:
    student = ", ".join(s)
    file.write(student)
    file.write("\n")
file.close()    

    

