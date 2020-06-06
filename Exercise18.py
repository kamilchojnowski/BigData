data = {":)": "😃", ":(": "😞"}

def get_emoji(x):
    return data.get(x, "Error 404")

print("Insert emoji: ")
print(get_emoji(input()))
