import math
import sys

class QuadraticEquation:
    
    def __init__(self, array):
        self.a = array[0]
        self.b = array[1]
        self.c = array[2]
    
    def getDelta(self) :
        return self.b*self.b - 4*self.a*self.c
    
    def isImaginary(self):
        return self.getDelta() < 0
    
    def getXs(self):
        xs = []
        if self.isImaginary():
            print('Rozwiązania zespolone')
            xs.append(f"-{self.b} - i{round(math.sqrt(-self.getDelta()), 3)} / {2*self.a}")
            xs.append(f"-{self.b} + i{round(math.sqrt(-self.getDelta()), 3)} / {2*self.a}")
        else:
            xs.append(-(round(math.sqrt(self.getDelta()), 3) + self.b)/(2*self.a))
            xs.append((round(math.sqrt(self.getDelta()), 3) - self.b)/(2*self.a))
        return xs
    
def getVariables():
    i = 0
    names = ['a', 'b', 'c']
    variables = []
    while i < 3:
        name = names[i]
        print(f'{name} = ', end='')
        try:
            inp = input()
            variable = float(inp)
        except ValueError:
            print(f'{inp} is not a valid number')
            continue
        variables.append(float(inp))
        i+=1
    return variables
                
        
print('Enter quadratic exuation variables')     
q = QuadraticEquation(getVariables())
xs = q.getXs()
print(f'x1 = {xs[0]}\nx2 = {xs[1]}')

    

