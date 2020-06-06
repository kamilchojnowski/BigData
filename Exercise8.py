print("Enter word to rotate: ")
word = input()
for w in word:
    print(chr(ord(w)+1), end='')