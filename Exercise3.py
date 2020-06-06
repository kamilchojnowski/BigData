def getAmount(i):
    return i if i > 0 else 'no more'

def getBottles(i):
    if i == 1:
        return f'{getAmount(i)} bottle'
    return f'{getAmount(i)} bottles'

for i in range(99, 0 , -1):
    print(f'{getBottles(i)} of beer on the wall, {getBottles(i)} of beer.')
    print(f'Take one down and pass it around, {getBottles(i-1)} of beer on the wall.')
print('No more bottles of beer on the wall, no more bottles of beer.')
print('Go to the store and buy some more, 99 bottles of beer on the wall.')