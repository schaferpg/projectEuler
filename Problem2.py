# Project Euler Problem 2
# https://projecteuler.net/problem=2

def fibonacciSequence(num1, num2, total, ceiling):
    
    num3 = num2+num1
    
    if (num3 > ceiling):
        return total
    
    if(num3%2==0):
        total+=num3
    
    return fibonacciSequence(num2,num3,total, ceiling)

total = 0
ceiling = 4000000

print(fibonacciSequence(0, 1, total, ceiling))

# Answer = 4613732
