import sys
import math
    
print('Enter money amount:', end='')
try:
    money = float(input())
except ValueError:
    print('Invalid data type')
    sys.exit()
    
if money < 0:
    print('Watch out, you are in the dept!')
    money = 0
    
iphone = 3000
print(f'Current price iPhoneX: {iphone}')
if iphone > money:
    print(f'You need {round(iphone - money, 2)} more to buy first iPhoneX')
else:
    print(f'You can afford {math.floor(money / iphone)} iPhoneX')
    print(f'You need {round(iphone - (money % iphone), 1)} more to buy the next one')