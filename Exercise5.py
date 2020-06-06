import sys
import math

def getDivisors(n) :
    divisors = []
    for i in range(1, math.floor(math.sqrt(n))):  
        if (n % i == 0) : 
            if (n / i == i) : 
                divisors.append(i) 
            else : 
                divisors.append(math.floor(i))
                divisors.append(math.floor(n/i))
    return sorted(divisors)

print("Enter numer to get divisors")
try:
    print('n = ', end='')
    n = int(input())
except ValueError:
    print('Invalid data')
    sys.exit()
    
print(getDivisors(n))