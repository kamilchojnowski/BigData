def getEvens(start, end):
    evens = []
    for i in range(start, end):
        if (i%2) == 0:
            evens.append(i)
    return evens

evens = getEvens(1, 201)
print(f'Even numbers: {evens}')
print(f'Even numbers count: {len(evens)}')
