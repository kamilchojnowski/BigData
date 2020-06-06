import math

def getPrimes(start, end):
    primes = []
    for number in range(start, end):
        if number > 1:
            for i in range(2, int(math.sqrt(number))+1):
                if (number%i) == 0:
                    break
            else:
                primes.append(number)
    return primes

print(getPrimes(1, 100))