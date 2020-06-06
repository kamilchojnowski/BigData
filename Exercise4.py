import sys

def factorial(n):
    return n*factorial(n-1) if n > 1 else 1

print('Enter value to factorial:')
try:
    print('n = ', end='')
    n = int(input())
except ValueError:
    print('Invalid data')
    sys.exit()
    
if (n<0):
    print('Invalid data')
    sys.exit()

print(factorial(n))
