def check_if_palindrome(data: str) -> bool:
    for i in range(int(len(data)/2)):
        if data[i] is not data[len(data)-i-1]:
            return False
    return True

print("insert a string")
data = input()
print(f"{data} is{'' if check_if_palindrome(data) else ' not'} a palindrome")

